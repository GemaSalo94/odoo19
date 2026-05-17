# -*- coding: utf-8 -*-
from odoo import models, fields, api

class Genero(models.Model):
    _name = 'libreria_v2.genero'
    _description = 'Género Literario'

    name = fields.Char(string='Nombre', required=True)
    descripcion = fields.Text(string='Descripción')
    #un genero puede pertenecer a muchos libros y un libro puede tener varios géneros
    libro_ids = fields.Many2many('libreria_v2.libro', string='Libros')