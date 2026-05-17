{
    'name': 'Gestión de Proyectos',
    'version': '1.0',
    'author': 'Gema Natalia Salcedo',
    'category': 'Project',
    'summary': 'Módulo para planificar proyectos, trabajos y actividades',
    'description': """
        Aplicación jerárquica para la gestión de proyectos, trabajos y actividades.
        Permite el control de estados, fechas, responsables y progreso.
    """,
    'depends': ['base', 'mail'], # 'mail' es para cumplir el requisito de adjuntar archivos
    'data': [
        # Seguridad (Obligatorio en Odoo, aunque el PDF no lo detalle, si no, no funciona)
        'security/ir.model.access.csv',
        
        # Vistas (El orden importa: de lo más básico a lo general)
        'views/estados_proyecto_view.xml',
        'views/proyecto_view.xml',
        'views/trabajo_view.xml',
        'views/actividad_view.xml',
        
        # Menús (Siempre al final para que las acciones de las vistas ya existan)
        'views/menus.xml',
    ],
    'demo': [
        # Archivos de demostración obligatorios 
        'demo/demo_estados.xml',
        'demo/demo_datos.xml',
    ],
    'installable': True,
    'application': True,
}