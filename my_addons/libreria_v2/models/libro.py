# -*- coding: utf-8 -*-
from odoo import models, fields, api

class Libro(models.Model):
    _name = 'libreria_v2.libro'
    _description = 'Libro'

    name = fields.Char(string='Título', required=True)
    fecha_publicacion = fields.Date(string='Fecha de Publicación')
    isbn = fields.Char(string='ISBN')
    descripcion = fields.Text(string='Descripción')
    portada = fields.Image(max_width=200, max_height=200)

    # RELACIONES
    # Un libro pertenece a un autor y muchos libros pueden ser de un autor
    autor_id = fields.Many2one('libreria_v2.autor', string='Autor')
    # Un libro puede tener varios géneros y un género tiene muchos libros
    genero_ids = fields.Many2many('libreria_v2.genero', string='Géneros')