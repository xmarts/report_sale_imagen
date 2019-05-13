# -*- coding: utf-8 -*-
{
    'name': "report_sale_img",

    'summary': """
        Modulo que muestra la imagen y tiempo de entrega en la orden de venta, compra y reportes""",

    'description': """
        Este modulo agrega la imagen del producto por cada linea al reporte de venta y compra, asi mismo se agregaron los campos de imagen a los presupuestos de estas mismas, ademas se anexa un campo de tiempo de entrega para cada linea de la orden de pedido.
    """,

    'author': "XMARTS",
    'website': "http://www.xmarts.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','sale','product','stock'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}