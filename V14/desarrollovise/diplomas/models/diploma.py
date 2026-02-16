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


class DiplomaUniversal(models.Model):
    _name = 'diploma'
    _description = 'Gestión de Diplomas y Actas de Grado'
    _order = 'create_date desc'
    _rec_name = 'nombre_completo'

    # --- CONTROL Y VISORES ---
    name = fields.Char(string="Referencia", default="Nuevo", readonly=True)
    state = fields.Selection([
        ('borrador', 'Borrador'),
        ('procesando', 'Procesando'),
        ('completado', 'Completado'),
        ('error', 'Error')
    ], string="Estado", default='borrador', readonly=True)

    # Carga de Archivos
    archivo_uno_subida = fields.Binary(string="Subir Diploma")
    nombre_uno = fields.Char(string="Nombre Archivo 1")
    archivo_dos_subida = fields.Binary(string="Subir Acta/Certificado")
    nombre_dos = fields.Char(string="Nombre Archivo 2")

    # Referencias a Attachments reales
    attachment_uno_id = fields.Many2one('ir.attachment', string='Adjunto Diploma', readonly=True)
    attachment_dos_id = fields.Many2one('ir.attachment', string='Adjunto Acta', readonly=True)

    # Visores HTML Gigantes
    visor_uno_html = fields.Html(string="Visor Diploma", compute="_compute_visores_html", sanitize=False)
    visor_dos_html = fields.Html(string="Visor Acta", compute="_compute_visores_html", sanitize=False)

    # --- DATOS EXTRAÍDOS ---
    nombre_completo = fields.Char(string="Nombre del Graduado", readonly=True)
    numero_identificacion = fields.Char(string="Identificación", readonly=True)
    titulo_obtenido = fields.Char(string="Título Otorgado", readonly=True)
    institucion_educativa = fields.Char(string="Institución Educativa", readonly=True)
    fecha_graduacion = fields.Date(string="Fecha de Grado", readonly=True)
    numero_acta = fields.Char(string="No. Acta", readonly=True)
    numero_libro = fields.Char(string="Libro", readonly=True)
    numero_folio = fields.Char(string="Folio", readonly=True)
    ciudad_grado = fields.Char(string="Ciudad/Municipio", readonly=True)
    codigo_dane = fields.Char(string="Código Dane", readonly=True)

    texto_extraido = fields.Text(string="JSON Crudo Gemini", readonly=True)
    error_mensaje = fields.Text(string="Error detectado", readonly=True)

    # --- LÓGICA DE VISORES ---
    @api.depends('attachment_uno_id', 'attachment_dos_id')
    def _compute_visores_html(self):
        base_url = self.env['ir.config_parameter'].sudo().get_param('web.base.url')
        for rec in self:
            # Visor 1
            if rec.attachment_uno_id:
                url1 = f"{base_url}/web/image/{rec.attachment_uno_id.id}"
                if rec.nombre_uno and rec.nombre_uno.lower().endswith('.pdf'):
                    rec.visor_uno_html = f'<div style="width:100%;"><embed src="{url1}" type="application/pdf" width="100%" height="1600px" style="border:3px solid #714B67;"/></div>'
                else:
                    rec.visor_uno_html = f'<div style="width:100%; text-align:center; border:3px solid #714B67;"><img src="{url1}" style="width:100%; height:auto;"/></div>'
            else:
                rec.visor_uno_html = False

            # Visor 2
            if rec.attachment_dos_id:
                url2 = f"{base_url}/web/image/{rec.attachment_dos_id.id}"
                if rec.nombre_dos and rec.nombre_dos.lower().endswith('.pdf'):
                    rec.visor_dos_html = f'<div style="width:100%;"><embed src="{url2}" type="application/pdf" width="100%" height="1600px" style="border:3px solid #714B67;"/></div>'
                else:
                    rec.visor_dos_html = f'<div style="width:100%; text-align:center; border:3px solid #714B67;"><img src="{url2}" style="width:100%; height:auto;"/></div>'
            else:
                rec.visor_dos_html = False

    def _optimizar_imagen(self, data_binaria):
        try:
            img = Image.open(BytesIO(data_binaria))
            if img.mode != 'L': img = ImageOps.grayscale(img)
            img = ImageEnhance.Contrast(img).enhance(1.4)
            img = ImageEnhance.Sharpness(img).enhance(2.0)
            buf = BytesIO();
            img.save(buf, format="PNG")
            return buf.getvalue()
        except:
            return data_binaria

    def _preparar_imagenes(self, attachment):
        if not attachment: return []
        data = base64.b64decode(attachment.datas)
        res = []
        if data.startswith(b'%PDF'):
            doc = fitz.open(stream=data, filetype="pdf")
            for page in doc:
                pix = page.get_pixmap(matrix=fitz.Matrix(2, 2))
                res.append(base64.b64encode(self._optimizar_imagen(pix.tobytes("png"))).decode('utf-8'))
            doc.close()
        else:
            res.append(base64.b64encode(self._optimizar_imagen(data)).decode('utf-8'))
        return res

    def procesar_diploma(self):
        self.ensure_one()
        if not self.attachment_uno_id and not self.attachment_dos_id: return

        try:
            self.state = 'procesando'
            self.env.cr.commit()

            ICP = self.env['ir.config_parameter'].sudo()
            api_key = ICP.get_param('gemini.api_key')
            model_name = ICP.get_param('gemini.model', 'gemini-2.5-flash')

            all_images = self._preparar_imagenes(self.attachment_uno_id) + self._preparar_imagenes(
                self.attachment_dos_id)

            prompt = """Analiza los documentos académicos. Extrae JSON: { "nombre_completo": "", "numero_identificacion": "", "titulo_obtenido": "", "institucion_educativa": "", "fecha_graduacion": "YYYY-MM-DD", "numero_acta": "", "numero_libro": "", "numero_folio": "", "ciudad_grado": "", "codigo_dane": "" }"""

            parts = [{"text": prompt}]
            for img in all_images:
                parts.append({"inline_data": {"mime_type": "image/png", "data": img}})

            url = f"https://generativelanguage.googleapis.com/v1beta/models/{model_name}:generateContent"
            response = requests.post(url, params={'key': api_key}, json={"contents": [{"parts": parts}]}, timeout=120)
            response.raise_for_status()

            raw_text = response.json()['candidates'][0]['content']['parts'][0]['text']
            json_str = raw_text[raw_text.find('{'):raw_text.rfind('}') + 1]
            datos = json.loads(json_str)

            if self.attachment_uno_id: self.attachment_uno_id.write({'description': json_str})

            def clean_date(val):
                return val if val and val not in ["null", "None", ""] else False

            self.write({
                'nombre_completo': datos.get('nombre_completo'),
                'numero_identificacion': (datos.get('numero_identificacion') or "").replace('.', ''),
                'titulo_obtenido': datos.get('titulo_obtenido'),
                'institucion_educativa': datos.get('institucion_educativa'),
                'codigo_dane': datos.get('codigo_dane'),
                'fecha_graduacion': clean_date(datos.get('fecha_graduacion')),
                'numero_acta': datos.get('numero_acta'),
                'numero_libro': datos.get('numero_libro'),
                'numero_folio': datos.get('numero_folio'),
                'ciudad_grado': datos.get('ciudad_grado'),
                'texto_extraido': raw_text,
                'state': 'completado'
            })
        except Exception as e:
            self.write({'state': 'error', 'error_mensaje': str(e)})

    @api.model
    def create(self, vals):
        if vals.get('name', 'Nuevo') == 'Nuevo':
            vals['name'] = self.env['ir.sequence'].next_by_code('diploma') or 'Nuevo'

        archivo1 = vals.get('archivo_uno_subida')
        archivo2 = vals.get('archivo_dos_subida')

        res = super(DiplomaUniversal, self).create(vals)

        if archivo1:
            att1 = self.env['ir.attachment'].create({
                'name': vals.get('nombre_uno', 'diploma'), 'datas': archivo1,
                'res_model': self._name, 'res_id': res.id, 'type': 'binary',
            })
            res.write({'attachment_uno_id': att1.id, 'archivo_uno_subida': False})

        if archivo2:
            att2 = self.env['ir.attachment'].create({
                'name': vals.get('nombre_dos', 'acta'), 'datas': archivo2,
                'res_model': self._name, 'res_id': res.id, 'type': 'binary',
            })
            res.write({'attachment_dos_id': att2.id, 'archivo_dos_subida': False})

        if archivo1 or archivo2:
            res.procesar_diploma()
        return res

    def write(self, vals):
        archivo1 = vals.get('archivo_uno_subida')
        archivo2 = vals.get('archivo_dos_subida')
        res = super(DiplomaUniversal, self).write(vals)

        if archivo1:
            for rec in self:
                if rec.attachment_uno_id: rec.attachment_uno_id.unlink()
                att1 = self.env['ir.attachment'].create({
                    'name': vals.get('nombre_uno', rec.nombre_uno or 'diploma'), 'datas': archivo1,
                    'res_model': self._name, 'res_id': rec.id, 'type': 'binary',
                })
                rec.write({'attachment_uno_id': att1.id, 'archivo_uno_subida': False})

        if archivo2:
            for rec in self:
                if rec.attachment_dos_id: rec.attachment_dos_id.unlink()
                att2 = self.env['ir.attachment'].create({
                    'name': vals.get('nombre_dos', rec.nombre_dos or 'acta'), 'datas': archivo2,
                    'res_model': self._name, 'res_id': rec.id, 'type': 'binary',
                })
                rec.write({'attachment_dos_id': att2.id, 'archivo_dos_subida': False})

        if archivo1 or archivo2:
            for rec in self: rec.procesar_diploma()
        return res