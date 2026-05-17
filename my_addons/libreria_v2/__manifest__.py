{
    'name': "libreria_v2 (Gema Natalia Salcedo)",

    'summary': "Modulo de libreria",

    'description': """
    Modulo de gestion de libreria del tema 5 de la modalidad de desarrollo 
    de aplicaciones Multiplataforma E-learning
    """,

    'author': "Gema Natalia Salcedo",
    'website': "https://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/autor.xml',
        'views/genero.xml',
        'views/libro.xml',
        'views/menus.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}

