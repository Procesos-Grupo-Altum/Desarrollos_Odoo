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


class CertificadoSeguridad(models.Model):
    _name = 'certificado.seguridad'
    _description = 'Certificado de Seguridad Privada'
    _order = 'create_date desc'
    _rec_name = 'name'

    # --- CONTROL Y VISOR ---
    name = fields.Char(string="Referencia", default="Nuevo", readonly=True)
    state = fields.Selection([
        ('borrador', 'Borrador'),
        ('procesando', 'Procesando'),
        ('completado', 'Completado'),
        ('error', 'Error')
    ], string="Estado", default='borrador', readonly=True)

    archivo_subida = fields.Binary(string="Subir Archivo", help="Cargue PDF o Imagen aquí")
    nombre_archivo = fields.Char(string="Nombre del Archivo")
    attachment_id = fields.Many2one('ir.attachment', string='Adjunto Real', readonly=True)
    visualizacion_html = fields.Html(string="Visor", compute="_compute_visualizacion_html", sanitize=False)

    # --- CAMPOS DE DATOS ---
    numero_cedula = fields.Char(string="Número de Cédula")
    nombre_completo = fields.Char(string="Nombre Completo")
    nci = fields.Char(string="NCI")
    nro_registro = fields.Char(string="NRO (Registro)")
    nombre_curso = fields.Char(string="Nombre del Curso")
    ciudad_curso = fields.Char(string="Ciudad del Curso")
    intensidad_horaria = fields.Char(string="Intensidad Horaria")
    tipo_arma = fields.Char(string="Tipo de Arma")

    fecha_inicio = fields.Date(string="Fecha Inicio")
    fecha_fin = fields.Date(string="Fecha Fin")
    fecha_expedicion = fields.Date(string="Fecha Expedición")
    fecha_vencimiento = fields.Date(string="Fecha Vencimiento")
    fecha_practica = fields.Date(string="Fecha de Práctica")
    fecha_resolucion = fields.Date(string="Fecha de Resolución")

    lugar_expedicion = fields.Char(string="Lugar de Expedición")
    direccion_expedicion = fields.Char(string="Dirección de Expedición")
    libro = fields.Char(string="Libro")
    folio = fields.Char(string="Folio")
    acta = fields.Char(string="Acta")

    academia = fields.Char(string="Nombre de la Institución")
    nit = fields.Char(string="NIT")
    licencia = fields.Char(string="Licencia")
    resolucion_licencia = fields.Char(string="Resolución Licencia")
    representante_legal = fields.Char(string="Representante Legal")
    nombre_directora = fields.Char(string="Nombre de Directora/Director")
    pagina_web = fields.Char(string="Página Web")

    dias_para_vencer = fields.Integer(string="Días para Vencer", compute='_compute_vigencia_datos', store=True)
    vigencia_state = fields.Selection([
        ('vigente', 'Vigente'),
        ('por_vencer', 'Por Vencer'),
        ('vencido', 'Vencido')
    ], string="Estado de Vigencia", compute='_compute_vigencia_datos', store=True)

    texto_extraido = fields.Text(string="Respuesta Gemini (JSON)", readonly=True)
    error_mensaje = fields.Text(string="Mensaje de Error", readonly=True)

    # --- VISUALIZACIÓN GIGANTE ---
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

    @api.depends('fecha_vencimiento')
    def _compute_vigencia_datos(self):
        today = fields.Date.today()
        for rec in self:
            if rec.fecha_vencimiento:
                delta = rec.fecha_vencimiento - today
                rec.dias_para_vencer = delta.days
                if rec.dias_para_vencer > 30:
                    rec.vigencia_state = 'vigente'
                elif rec.dias_para_vencer > 0:
                    rec.vigencia_state = 'por_vencer'
                else:
                    rec.vigencia_state = 'vencido'
            else:
                rec.dias_para_vencer = 0;
                rec.vigencia_state = 'vencido'

    def reiniciar_proceso(self):
        self.write({'state': 'borrador', 'error_mensaje': False, 'texto_extraido': False})

    def _optimizar_imagen(self, data_binaria):
        try:
            img = Image.open(BytesIO(data_binaria))
            if img.mode != 'L': img = ImageOps.grayscale(img)
            img = ImageEnhance.Contrast(img).enhance(1.5)
            img = ImageEnhance.Sharpness(img).enhance(2.0)
            buffer = BytesIO()
            img.save(buffer, format="PNG")
            return buffer.getvalue()
        except:
            return data_binaria

    def procesar_certificado(self):
        self.ensure_one()
        if not self.attachment_id: return

        try:
            self.state = 'procesando'
            self.env.cr.commit()

            archivo_data = base64.b64decode(self.attachment_id.datas)

            if self.nombre_archivo and self.nombre_archivo.lower().endswith('.pdf'):
                doc = fitz.open(stream=archivo_data, filetype="pdf")
                pix = doc.load_page(0).get_pixmap(matrix=fitz.Matrix(2, 2))
                archivo_data = pix.tobytes("png")
                doc.close()

            archivo_data_opt = self._optimizar_imagen(archivo_data)

            ICP = self.env['ir.config_parameter'].sudo()
            api_key = ICP.get_param('gemini.api_key')
            model_name = ICP.get_param('gemini.model', 'gemini-2.5-flash')

            img_b64 = base64.b64encode(archivo_data_opt).decode('utf-8')
            prompt = """Analiza este certificado y extrae JSON estricto: {"numero_cedula":"", "nombre_completo":"", "nci":"", "nro_registro":"", "nombre_curso":"", "intensidad_horaria":"", "ciudad_curso":"", "tipo_arma":"", "fecha_inicio":"YYYY-MM-DD", "fecha_fin":"YYYY-MM-DD", "fecha_practica":"YYYY-MM-DD", "fecha_expedicion":"YYYY-MM-DD", "fecha_vencimiento":"YYYY-MM-DD", "academia":"", "nit":"", "pagina_web":"", "lugar_expedicion":"", "direccion_expedicion":"", "licencia":"", "resolucion_licencia":"", "fecha_resolucion":"YYYY-MM-DD", "representante_legal":"", "nombre_directora":"", "libro":"", "folio":"", "acta":""}"""

            url = f"https://generativelanguage.googleapis.com/v1beta/models/{model_name}:generateContent"
            payload = {"contents": [
                {"parts": [{"text": prompt}, {"inline_data": {"mime_type": "image/png", "data": img_b64}}]}]}

            response = requests.post(url, params={'key': api_key}, json=payload, timeout=60)
            response.raise_for_status()

            raw_text = response.json()['candidates'][0]['content']['parts'][0]['text']
            json_str = raw_text[raw_text.find('{'):raw_text.rfind('}') + 1]
            datos = json.loads(json_str)

            self.attachment_id.write({'description': json_str})

            def clean_d(v):
                return v if v and v not in ["null", "None", ""] else False

            self.write({
                'numero_cedula': datos.get('numero_cedula'),
                'nombre_completo': datos.get('nombre_completo'),
                'nci': datos.get('nci'),
                'nro_registro': datos.get('nro_registro'),
                'nombre_curso': datos.get('nombre_curso'),
                'intensidad_horaria': datos.get('intensidad_horaria'),
                'ciudad_curso': datos.get('ciudad_curso'),
                'tipo_arma': datos.get('tipo_arma'),
                'fecha_inicio': clean_d(datos.get('fecha_inicio')),
                'fecha_fin': clean_d(datos.get('fecha_fin')),
                'fecha_practica': clean_d(datos.get('fecha_practica')),
                'fecha_expedicion': clean_d(datos.get('fecha_expedicion')),
                'fecha_vencimiento': clean_d(datos.get('fecha_vencimiento')),
                'academia': datos.get('academia'),
                'nit': datos.get('nit'),
                'pagina_web': datos.get('pagina_web'),
                'lugar_expedicion': datos.get('lugar_expedicion'),
                'direccion_expedicion': datos.get('direccion_expedicion'),
                'licencia': datos.get('licencia'),
                'resolucion_licencia': datos.get('resolucion_licencia'),
                'fecha_resolucion': clean_d(datos.get('fecha_resolucion')),
                'representante_legal': datos.get('representante_legal'),
                'nombre_directora': datos.get('nombre_directora'),
                'libro': datos.get('libro'),
                'folio': datos.get('folio'),
                'acta': datos.get('acta'),
                'state': 'completado',
                'texto_extraido': raw_text
            })
        except Exception as e:
            self.write({'state': 'error', 'error_mensaje': str(e)})

    @api.model
    def create(self, vals):
        if vals.get('name', 'Nuevo') == 'Nuevo':
            vals['name'] = self.env['ir.sequence'].next_by_code('certificado.seguridad') or 'Nuevo'
        archivo = vals.get('archivo_subida')
        res = super(CertificadoSeguridad, self).create(vals)
        if archivo:
            att = self.env['ir.attachment'].create({
                'name': vals.get('nombre_archivo', 'certificado'),
                'datas': archivo,
                'res_model': self._name, 'res_id': res.id, 'type': 'binary',
            })
            res.write({'attachment_id': att.id, 'archivo_subida': False})
            res.procesar_certificado()
        return res

    def write(self, vals):
        archivo = vals.get('archivo_subida')
        res = super(CertificadoSeguridad, self).write(vals)
        if archivo:
            for rec in self:
                if rec.attachment_id: rec.attachment_id.unlink()
                att = self.env['ir.attachment'].create({
                    'name': vals.get('nombre_archivo', 'certificado'),
                    'datas': archivo,
                    'res_model': self._name, 'res_id': rec.id, 'type': 'binary',
                })
                rec.write({'attachment_id': att.id, 'archivo_subida': False})
                rec.procesar_certificado()
        return res