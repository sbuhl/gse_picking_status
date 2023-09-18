# -*- coding: utf-8 -*-

{
    'name': 'Delivery and Reception Status',
    'author': "Sébastien Bühl",
    'website': "http://www.buhl.be",
    'version': '0.2',
    'category': 'Hidden',
    'license': 'LGPL-3',
    'summary': 'Sales Orders, Purchase Order & Delivery Control',
    'description': """
        Display the status of the picking. 
        Only for storable products, obviously.
        Not | Partially | Fully Received/Delivered 
""",
    'depends': ['sale_stock', 'purchase', 'stock_account'],
    'data': [
        #'views/gse_sale_order_view.xml',
        #'views/gse_purchase_order_view.xml',
            
    ],
    'installable': True,
    
}