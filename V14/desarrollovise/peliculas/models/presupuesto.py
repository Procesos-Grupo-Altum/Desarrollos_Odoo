# -*- coding:utf-8 -*-
# from email.policy import default,logging
import logging
from email.policy import default

from setuptools.dist import sequence

from odoo import fields, models, api
from odoo.exceptions import UserError

logger = logging.getLogger(__name__)


class Presupuesto(models.Model):
    _name = "presupuesto"
    _inherit=['mail.thread','mail.activity.mixin','image.mixin']

    @api.depends('detalle_ids')
    def _compute_total(self):
        for record in self:
            sub_total = 0
            for linea in record.detalle_ids:
                sub_total += linea.importe
            record.base = sub_total
            record.impuestos = sub_total * 0.19
            record.total = sub_total * 1.19

    name = fields.Char(string="Pelicula")
    clasificacion = fields.Selection(selection=[
        ('G','G'), #Publico general
        ('PG','PG'), # Se recomienda la compañia de un adulto
        ('PG-13','PG13'), # Mayores de 13
        ('R','R'), #  En compañia de un adulto obligatorio
        ('NC-17','NC-17'), # Mayores de 18
    ],string="Clasificación")
    dsc_clasificacion = fields.Char(string="Descripcion clasificacion")
    fecha_estreno = fields.Date(string="Fecha estreno")
    puntuacion = fields.Integer(string="Puntuacion", related="puntuacion2")
    puntuacion2 = fields.Integer(string="Puntuacion2")
    active = fields.Boolean(string="Activo", default=True)
    director_id = fields.Many2one(
        comodel_name="res.partner",
        string="Director"
    )
    categoria_director_id=fields.Many2one(
        comodel_name="res.partner.category",
        string="Categoria Director",
        default=lambda self: self.env.ref('peliculas.category_director')
    # default = lambda self: self.env['res.partner.category'].search([('name', '=', 'Director')])
    )
    genero_ids=fields.Many2many(
        comodel_name="genero",
        string="Generos"
    )
    vista_general = fields.Text(string="Descripción")
    link_trailer = fields.Char(string="Trailer")
    es_libro = fields.Boolean(string="Versión Libro")
    libro =fields.Binary(string="Libro")
    libro_filename = fields.Char(string="Nombre del libro")

    state = fields.Selection(selection=[
        ('borrador','Borrador'),
        ('aprobado','Aprobado'),
        ('cancelado','Cacelado'),


    ],default='borrador' ,string="Estados", copy=False)
    fec_aprobado = fields.Datetime(string='Fecha aprobado', copy=False)
    num_presupuesto = fields.Char(string='Numero presupuesto', copy=False)
    fec_creacion = fields.Datetime(string='Fecha creacion', copy=False, default=lambda self: fields.Datetime.now())
    actor_ids = fields.Many2many(
        comodel_name="res.partner",
        string="Actores"
    )

    categoria_actor_id = fields.Many2one(
        comodel_name="res.partner.category",
        string="Categoria Actor",
        default=lambda self: self.env.ref('peliculas.category_actor')

    )
    opinion = fields.Html(string="Opinion")

    detalle_ids = fields.One2many(
        comodel_name='presupuesto.detalle',
        inverse_name='presupuesto_id',
        string="Detalles"
    )
    campos_ocultos= fields.Boolean(string='Campos ocultos')
    currency_id = fields.Many2one(
        comodel_name='res.currency',
        string='Moneda',
        default=lambda self: self.env.company.currency_id.id
    )
    terminos = fields.Text(string='Términos')
    base = fields.Monetary(string='Base imponible', compute='_compute_total')
    impuestos = fields.Monetary(string='Impuestos', compute='_compute_total')
    total = fields.Monetary(string='Total', compute='_compute_total')



    def aprobar_presupuesto(self):
        logger.info('Entro a la funcion Aprobar presupuesto')
        # logger.warning('Hola mundo')
        # logger.error('Hola mundo')
        self.state='aprobado'
        self.fec_aprobado = fields.Datetime.now()

    def cancelar_presupuesto(self):
        logger.info('Entro a la funcion Cancelar presupuesto')
        self.state = 'cancelado'

    def unlink(self):
        logger.info('Se disparo la funcion eliminar registro')
        for record in self:
            if record.state != 'cancelado':
                logger.info('No se puede eliminar el registro por que no se encuentra en el estado cancelado')
                raise UserError('No se puede eliminar el registro por que no se encuentra en el estado cancelado')
            super(Presupuesto, record).unlink()

    @api.model
    def create(self, variables):
        logger.info('************ variables: {0}'.format(variables))
        sequence_obj = self.env['ir.sequence']
        correlativo = sequence_obj.next_by_code('secuencia.presupuesto.pelicula')
        variables['num_presupuesto']=correlativo
        return super(Presupuesto, self).create(variables)

    def write(self, variables):
        logger.info('************ variables: {0}'.format(variables))
        if 'clasificacion' in variables:
            raise UserError('la clasificacion no se puede cambiar')
        return super(Presupuesto, self).write(variables)

    def copy(self, default=None):
        default = dict(default or {})
        default['name'] = self.name + ' (Copia)'
        default['puntuacion2'] = 1
        return super(Presupuesto, self).copy(default)

    @api.onchange('clasificacion')
    def _onchange_clasificacion(self):
        if self.clasificacion:
            if self.clasificacion == 'G':
                self.dsc_clasificacion ='Publico general'
            if self.clasificacion == 'PG':
                self.dsc_clasificacion ='Se recomienda la compañia de un adulto'
            if self.clasificacion == 'PG-13':
                self.dsc_clasificacion = 'Mayores de 13'
            if self.clasificacion == 'R':
                self.dsc_clasificacion = 'En compañia de un adulto obligatorio'
            if self.clasificacion == 'NC-17':
                self.dsc_clasificacion = 'Mayores de 18'
        else:
            self.dsc_clasificacion = False


class PresupuestoDetalle(models.Model):
    _name = "presupuesto.detalle"

    presupuesto_id = fields.Many2one(
        comodel_name='presupuesto',
        string='Presupuesto'
    )

    name = fields.Many2one(
        comodel_name = 'recurso.cinematografico', #producto.product
        string='Recurso'
    )
    descripcion = fields.Char( string='Descripcion', related='name.descripcion')
    contacto_id = fields.Many2one(
        comodel_name='res.partner',
        string='Contacto',
        related='name.contacto_id'
    )
    activity_exception_icon = fields.Char(String='Icono', readonly=True, tracking=0, ),
    imagen = fields.Binary(string='Imagen', related='name.imagen')
    cantidad = fields.Float(string='Cantidad', default=1.0, digits=(16,4))
    precio = fields.Float(string='Precio', digits=('Product Price'))
    importe = fields.Monetary(string='Importe')
    currency_id = fields.Many2one(
        comodel_name='res.currency',
        string='Moneda',
        related='presupuesto_id.currency_id'
    )

    @api.onchange('name')
    def _onchange_name(self):
        if self.name:
            self.precio=self.name.precio

    @api.onchange('cantidad', 'precio')
    def _onchange_importe(self):
        # if self.name:
            self.importe = self.cantidad * self.precio


