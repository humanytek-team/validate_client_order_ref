# -*- coding: utf-8 -*-
{
    'name': 'Valida referencia de cliente en pedidos de venta',
    'version': '1.1',
    'summary': 'Al confirmar un pedido de venta se valida que no haya algún otro pedido con la misma referencia.',
    'category': 'Denker',
    'description': """
    Al confirmar un pedido de venta se valida que no haya algún otro pedido con la misma referencia del cliente.
    """,
    'author': 'Humanytek',
    'website': 'http://www.humanytek.com',
    'depends': ['sale'],
    'data': [
        'sale_order.xml',
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
}
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
