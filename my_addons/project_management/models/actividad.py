from odoo import models, fields, api, exceptions

class Actividad(models.Model):
    _name = 'project_management.actividad'
    _description = 'Actividad del Trabajo'
    # Heredamos de mail para poder adjuntar archivos 
    _inherit = ['mail.thread', 'mail.activity.mixin']

    # Campos Básicos
    name = fields.Char(string='Nombre de la actividad', required=True, tracking=True)
    detalle = fields.Text(string='Detalle de la tarea')
    
    # Fechas
    fecha_inicio = fields.Date(string='Inicio planificado')
    fecha_fin = fields.Date(string='Fin planificado')
    
    # Estado 
    estado = fields.Selection([
        ('pendiente', 'Pendiente'),
        ('curso', 'En curso'),
        ('revision', 'En revisión'),
        ('finalizada', 'Finalizada'),
        ('cancelada', 'Cancelada')
    ], string='Estado de la actividad', default='pendiente', tracking=True)
    
    # Avance 
    avance = fields.Float(string='Avance individual (%)', default=0.0, tracking=True)

    # Relaciones 
    trabajo_id = fields.Many2one('project_management.trabajo', string='Trabajo al que pertenece', ondelete='cascade', required=True)
    responsable_id = fields.Many2one('res.users', string='Persona que la realiza', tracking=True)

    # RESTRICCIÓN: Control de fechas 
    @api.constrains('fecha_inicio', 'fecha_fin', 'trabajo_id')
    def _check_fechas(self):
        for record in self:
            if record.trabajo_id and record.fecha_inicio and record.fecha_fin:
                if record.trabajo_id.fecha_inicio and record.fecha_inicio < record.trabajo_id.fecha_inicio:
                    raise exceptions.ValidationError("La fecha de inicio de la actividad no puede ser anterior a la de su trabajo.")
                if record.trabajo_id.fecha_fin and record.fecha_fin > record.trabajo_id.fecha_fin:
                    raise exceptions.ValidationError("La fecha de fin de la actividad no puede ser posterior a la de su trabajo.")