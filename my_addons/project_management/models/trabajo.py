from odoo import models, fields, api, exceptions

class Trabajo(models.Model):
    _name = 'project_management.trabajo'
    _description = 'Trabajo del Proyecto'
    # Heredamos de mail para poder adjuntar archivos en los trabajos
    _inherit = ['mail.thread', 'mail.activity.mixin']

    # Campos Básicos 
    name = fields.Char(string='Descripción del trabajo', required=True, tracking=True)
    fecha_inicio = fields.Date(string='Fecha de inicio')
    fecha_fin = fields.Date(string='Fecha de finalización')
    
    # Selecciones
    estado = fields.Selection([
        ('pendiente', 'Pendiente'),
        ('progreso', 'En progreso'),
        ('revision', 'En revisión'),
        ('finalizado', 'Finalizado')
    ], string='Estado actual', default='pendiente', tracking=True)
    
    importancia = fields.Selection([
        ('baja', 'Baja'),
        ('media', 'Media'),
        ('alta', 'Alta'),
        ('urgente', 'Urgente')
    ], string='Importancia', default='media')

    # Relaciones 
    proyecto_id = fields.Many2one('project_management.proyecto', string='Proyecto', ondelete='cascade', required=True)
    responsable_id = fields.Many2one('res.users', string='Responsable o técnico asignado')
    
    # Relación con las actividades (Un trabajo tiene muchas actividades)
    actividad_ids = fields.One2many('project_management.actividad', 'trabajo_id', string='Actividades')

    # Campo Computado para el avance
    avance = fields.Float(string='Avance individual (%)', compute='_compute_avance', store=True)

    @api.depends('actividad_ids.avance', 'actividad_ids.estado')
    def _compute_avance(self):
        """ Calcula la media de avance de las actividades y actualiza el estado automáticamente """
        for record in self:
            if record.actividad_ids:
                # 1. Cálculo de la media del avance 
                total_avance = sum(act.avance for act in record.actividad_ids)
                record.avance = total_avance / len(record.actividad_ids)
                
                # 2. Cambio de estado automático: Si todas están finalizadas, el trabajo se finaliza 
                todas_finalizadas = all(act.estado == 'finalizada' for act in record.actividad_ids)
                if todas_finalizadas and record.estado != 'finalizado':
                    record.estado = 'finalizado'
            else:
                record.avance = 0.0

    # RESTRICCIÓN: Control de fechas 
    @api.constrains('fecha_inicio', 'fecha_fin', 'proyecto_id')
    def _check_fechas(self):
        for record in self:
            if record.proyecto_id and record.fecha_inicio and record.fecha_fin:
                if record.proyecto_id.fecha_inicio and record.fecha_inicio < record.proyecto_id.fecha_inicio:
                    raise exceptions.ValidationError("La fecha de inicio del trabajo no puede ser anterior a la del proyecto.")
                if record.proyecto_id.fecha_fin and record.fecha_fin > record.proyecto_id.fecha_fin:
                    raise exceptions.ValidationError("La fecha de fin del trabajo no puede ser posterior a la del proyecto.")