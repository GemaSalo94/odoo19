# -*- coding: utf-8 -*- 
from odoo import models, fields, api  

class Autor(models.Model):     
    _name = 'libreria_v2.autor'     
    _description = 'Autor'      
    name = fields.Char(string='Nombre', required=True)     

    #RELACIONES
    #un autor tiene muchos libros y un libro SOLO puede pertenecer a un autor     
    libro_ids = fields.One2many('libreria_v2.libro', 'autor_id', string='Libros')  
    #campo computados 
    numLibros = fields.Integer(string='Número de Libros', 
    compute='_compute_contar_libros', store=False)

    # función para campo computado que cuenta el número de libros del autor
    @api.depends('libro_ids')
    def _compute_contar_libros(self):
        for autor in self:
            autor.numLibros = len(autor.libro_ids)