{
    'name': 'sale_order_fee',
    'version': '1.3',
    'description': 'Calculo y control del Fee en ordenes de venta',
    'summary': 'Calculo y control del Fee en ordenes de venta',
    'license': 'LGPL-3',
    'author': "Ingenio Solutions",
    'website': "https://www.ingeniosolutions.com.ar",
    'depends': [
        'sale_management',
        'bright_solutions_sv'
    ],
    'data': [
        'views/res_config_settings.xml',
        'views/res_partner.xml',
        'views/sale_order.xml',
        'views/sale_order_template.xml',
    ],
    'auto_install': True,
    'application': False,
}
