from odoo import models, fields

class EstadoProyecto(models.Model):
    # _name es el identificador único de esta tabla en la base de datos
    _name = 'project_management.estado'
    _description = 'Estados del Proyecto'

    # Campos de la base de datos
    name = fields.Char(string='Nombre del Estado', required=True)
    sequence = fields.Integer(string='Secuencia', default=10, help="Para ordenar los estados")