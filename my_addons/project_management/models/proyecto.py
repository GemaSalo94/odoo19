from odoo import models, fields, api, exceptions

class Proyecto(models.Model):
    _name = 'project_management.proyecto'
    _description = 'Proyecto Principal'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    # --- CAMPOS BÁSICOS ---
    name = fields.Char(string='Nombre del proyecto', required=True, tracking=True)
    descripcion = fields.Text(string='Descripción general')
    fecha_inicio = fields.Date(string='Fecha de inicio')
    fecha_fin = fields.Date(string='Fecha de fin')
    responsable_id = fields.Many2one('res.users', string='Responsable del proyecto')

    # AÑADIMOS EL CAMPO PRIORIDAD QUE PIDE EL PDF
    prioridad = fields.Selection([
        ('0', 'Baja'),
        ('1', 'Media'),
        ('2', 'Alta'),
        ('3', 'Urgente'),
    ], string='Prioridad', default='1', tracking=True)

    estado_id = fields.Many2one(
        'project_management.estado',
        string='Estado del proyecto',
        compute='_compute_estado_automatico',
        store=True,
        readonly=False,
        tracking=True
    )

    trabajo_ids = fields.One2many('project_management.trabajo', 'proyecto_id', string='Trabajos')
    progreso = fields.Float(string='Porcentaje de avance', compute='_compute_progreso', store=True)

    # --- CÁLCULO DE AVANCE ---
    @api.depends('trabajo_ids.avance', 'trabajo_ids.estado')
    def _compute_progreso(self):
        for record in self:
            if record.trabajo_ids:
                total_avance = sum(trabajo.avance for trabajo in record.trabajo_ids)
                record.progreso = total_avance / len(record.trabajo_ids)
            else:
                record.progreso = 0.0

    # --- DISPARADOR EN CADENA ---
    @api.depends('progreso', 'trabajo_ids.estado')
    def _compute_estado_automatico(self):
        for proyecto in self:
            est_fin  = self.env['project_management.estado'].search([('name', 'ilike', 'Finalizado')], limit=1)
            est_ejec = self.env['project_management.estado'].search([('name', 'ilike', 'En ejecución')], limit=1)
            est_borr = self.env['project_management.estado'].search([('name', 'ilike', 'Borrador')], limit=1)

            todos_finalizados = (
                bool(proyecto.trabajo_ids) and
                all(t.estado == 'finalizado' for t in proyecto.trabajo_ids)
            )

            if proyecto.progreso >= 100.0 or todos_finalizados:
                if est_fin:
                    proyecto.estado_id = est_fin
            elif proyecto.progreso > 0:
                if not proyecto.estado_id or proyecto.estado_id.name == 'Borrador':
                    if est_ejec:
                        proyecto.estado_id = est_ejec
            else:
                if est_borr:
                    proyecto.estado_id = est_borr

    # --- RESTRICCIONES ---
    @api.constrains('estado_id')
    def _check_estado_finalizado(self):
        for record in self:
            if record.estado_id and record.estado_id.name == 'Finalizado' and record.progreso < 100:
                raise exceptions.ValidationError("No puedes finalizar el proyecto manualmente si el progreso no es del 100%.")

    def unlink(self):
        for record in self:
            if record.trabajo_ids and record.estado_id and record.estado_id.name != 'Borrador':
                raise exceptions.UserError("No se puede eliminar un proyecto con trabajos asociados salvo que esté en estado Borrador.")
        return super(Proyecto, self).unlink()