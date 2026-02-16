# -*- coding: utf-8 -*-
import base64
import json
import logging
import requests
import fitz  # PyMuPDF
from io import BytesIO
from PIL import Image, ImageOps, ImageEnhance
from odoo import models, fields, api, _
from odoo.exceptions import ValidationError

_logger = logging.getLogger(__name__)


class CedulaExtractor(models.Model):
    _name = 'cedula.extractor'
    _description = 'Extractor de Cédulas Colombianas'
    _rec_name = 'nombre_completo'

    # --- CONTROL Y VISOR ---
    name = fields.Char(string='Referencia', default='Nuevo', readonly=True)
    estado = fields.Selection([
        ('borrador', 'Borrador'),
        ('procesando', 'Procesando'),
        ('completado', 'Completado'),
        ('error', 'Error'),
    ], string='Estado', default='borrador')

    archivo_subida = fields.Binary('Subir Archivo', help="Cargue PDF o Imagen")
    nombre_archivo = fields.Char('Nombre del Archivo')
    attachment_id = fields.Many2one('ir.attachment', string='Adjunto Real', readonly=True)
    visualizacion_html = fields.Html(string="Visor Documento", compute="_compute_visualizacion_html", sanitize=False)

    # --- DATOS EXTRAÍDOS ---
    numero_cedula = fields.Char('Número de Cédula', readonly=True)
    nombre_completo = fields.Char('Nombre Completo', readonly=True)
    nombres = fields.Char('Nombres', readonly=True)
    apellidos = fields.Char('Apellidos', readonly=True)
    first_name = fields.Char('Primer Nombre', readonly=True)
    second_name = fields.Char('Segundo Nombre', readonly=True)
    first_surname = fields.Char('Primer Apellido', readonly=True)
    second_surname = fields.Char('Segundo Apellido', readonly=True)
    fecha_nacimiento = fields.Char('Fecha Nacimiento', readonly=True)
    lugar_nacimiento_original = fields.Char('Lugar Nacimiento Original', readonly=True)
    municipio_nacimiento = fields.Char('Municipio Nacimiento', compute='_compute_lugares_desglosados', store=True)
    departamento_nacimiento = fields.Char('Departamento Nacimiento', compute='_compute_lugares_desglosados', store=True)
    estatura = fields.Char('Estatura', readonly=True)
    grupo_sanguineo = fields.Char('Grupo Sanguíneo', readonly=True)
    sexo = fields.Char('Sexo', readonly=True)
    fecha_expedicion = fields.Char('Fecha Expedición', readonly=True)
    lugar_expedicion_original = fields.Char('Lugar Expedición Original', readonly=True)
    municipio_expedicion = fields.Char('Municipio Expedición', compute='_compute_lugares_desglosados', store=True)
    departamento_expedicion = fields.Char('Departamento Expedición', compute='_compute_lugares_desglosados', store=True)
    foto_cedula = fields.Binary('Foto Extraída', readonly=True, attachment=True)
    tokens_totales = fields.Integer('Tokens', readonly=True)
    costo_estimado = fields.Float('Costo (USD)', readonly=True)
    respuesta_gemini = fields.Text('Respuesta JSON', readonly=True)
    error_mensaje = fields.Text('Mensaje de Error', readonly=True)

    @api.depends('attachment_id')
    def _compute_visualizacion_html(self):
        base_url = self.env['ir.config_parameter'].sudo().get_param('web.base.url')
        for rec in self:
            if rec.attachment_id:
                file_url = f"{base_url}/web/image/{rec.attachment_id.id}"
                if rec.nombre_archivo and rec.nombre_archivo.lower().endswith('.pdf'):
                    rec.visualizacion_html = f'<div style="width:100%;"><embed src="{file_url}" type="application/pdf" width="100%" height="1600px" style="border:3px solid #714B67;"/></div>'
                else:
                    rec.visualizacion_html = f'<div style="width:100%; text-align:center; border:3px solid #714B67; background:#eee;"><img src="{file_url}" style="width:100%; height:auto; display:block; margin:0 auto;"/></div>'
            else:
                rec.visualizacion_html = False

    @api.depends('lugar_nacimiento_original', 'lugar_expedicion_original')
    def _compute_lugares_desglosados(self):
        for rec in self:
            def extraer(texto):
                if not texto or '(' not in texto: return texto or '', ''
                parts = texto.split('(')
                return parts[0].strip(), parts[1].replace(')', '').strip()

            rec.municipio_nacimiento, rec.departamento_nacimiento = extraer(rec.lugar_nacimiento_original)
            rec.municipio_expedicion, rec.departamento_expedicion = extraer(rec.lugar_expedicion_original)

    def procesar_cedula(self):
        self.ensure_one()
        if not self.attachment_id: return

        try:
            self.estado = 'procesando'
            self.env.cr.commit()

            archivo_data = base64.b64decode(self.attachment_id.datas)

            if self.nombre_archivo and self.nombre_archivo.lower().endswith('.pdf'):
                doc = fitz.open(stream=archivo_data, filetype="pdf")
                pix = doc.load_page(0).get_pixmap(matrix=fitz.Matrix(2, 2))
                archivo_data = pix.tobytes("png")
                doc.close()

            ICP = self.env['ir.config_parameter'].sudo()
            api_key = ICP.get_param('gemini.api_key')
            # AQUÍ RESPETAMOS EL MODELO 2.5
            model_name = ICP.get_param('gemini.model', 'gemini-2.5-flash')

            if not api_key: raise ValidationError("Falta API Key de Gemini.")

            img_b64 = base64.b64encode(archivo_data).decode('utf-8')
            prompt = "Analiza esta cédula colombiana y extrae JSON estricto: numero_cedula, nombres, apellidos, fecha_nacimiento, lugar_nacimiento, estatura, grupo_sanguineo, sexo, fecha_expedicion, lugar_expedicion."

            # URL construida correctamente sin duplicar parámetros
            url = f"https://generativelanguage.googleapis.com/v1beta/models/{model_name}:generateContent"
            payload = {
                "contents": [{
                    "parts": [
                        {"text": prompt},
                        {"inline_data": {"mime_type": "image/png", "data": img_b64}}
                    ]
                }]
            }

            response = requests.post(url, params={'key': api_key}, json=payload, timeout=60)
            response.raise_for_status()

            res_json = response.json()
            if 'candidates' in res_json:
                raw_text = res_json['candidates'][0]['content']['parts'][0]['text']
                json_str = raw_text[raw_text.find('{'):raw_text.rfind('}') + 1]
                datos = json.loads(json_str)

                self.attachment_id.write({'description': json_str})

                n_list = (datos.get('nombres') or "").split()
                a_list = (datos.get('apellidos') or "").split()
                tokens = res_json.get('usageMetadata', {}).get('totalTokenCount', 0)

                self.write({
                    'estado': 'completado',
                    'numero_cedula': datos.get('numero_cedula'),
                    'nombres': datos.get('nombres'),
                    'apellidos': datos.get('apellidos'),
                    'nombre_completo': f"{datos.get('nombres')} {datos.get('apellidos')}".title(),
                    'first_name': n_list[0].title() if n_list else '',
                    'second_name': " ".join(n_list[1:]).title() if len(n_list) > 1 else '',
                    'first_surname': a_list[0].title() if a_list else '',
                    'second_surname': " ".join(a_list[1:]).title() if len(a_list) > 1 else '',
                    'fecha_nacimiento': datos.get('fecha_nacimiento'),
                    'lugar_nacimiento_original': datos.get('lugar_nacimiento'),
                    'estatura': datos.get('estatura'),
                    'grupo_sanguineo': datos.get('grupo_sanguineo'),
                    'sexo': datos.get('sexo'),
                    'fecha_expedicion': datos.get('fecha_expedicion'),
                    'lugar_expedicion_original': datos.get('lugar_expedicion'),
                    'respuesta_gemini': raw_text,
                    'tokens_totales': tokens,
                    'costo_estimado': (tokens / 1000000) * 0.15,
                    'name': f"CC {datos.get('numero_cedula')}"
                })
            else:
                raise ValidationError("Gemini no devolvió resultados válidos.")

        except Exception as e:
            self.write({'estado': 'error', 'error_mensaje': str(e)})

    @api.model
    def create(self, vals):
        archivo = vals.get('archivo_subida')
        res = super(CedulaExtractor, self).create(vals)
        if archivo:
            att = self.env['ir.attachment'].create({
                'name': vals.get('nombre_archivo', 'cedula'),
                'datas': archivo,
                'res_model': self._name, 'res_id': res.id, 'type': 'binary',
            })
            res.write({'attachment_id': att.id, 'archivo_subida': False})
            res.procesar_cedula()
        return res

    def write(self, vals):
        archivo = vals.get('archivo_subida')
        res = super(CedulaExtractor, self).write(vals)
        if archivo:
            for rec in self:
                if rec.attachment_id: rec.attachment_id.unlink()
                att = self.env['ir.attachment'].create({
                    'name': vals.get('nombre_archivo', rec.nombre_archivo or 'cedula'),
                    'datas': archivo,
                    'res_model': self._name, 'res_id': rec.id, 'type': 'binary',
                })
                rec.write({'attachment_id': att.id, 'archivo_subida': False})
                rec.procesar_cedula()
        return res

    def reiniciar_proceso(self):
        self.write({'estado': 'borrador', 'numero_cedula': False, 'name': 'Nuevo', 'respuesta_gemini': False,
                    'error_mensaje': False})