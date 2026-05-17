from odoo import models, fields, api


class libro(models.Model):
    _name = 'libreria.libro'
    _description = 'Modelo para la clase libro'

    nombre_libro = fields.Char()
    numPaginas = fields.Integer()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100

