# -*- coding: utf-8 -*-

from odoo import api, fields, models


class SaleOrder(models.Model):
    _inherit = "sale.order"

    delivery_status = fields.Selection([
        ('pending', 'Not Delivered'),
        ('partial', 'Partially Delivered'),
        ('full', 'Fully Delivered'),
    ], string='Delivery Status', compute='_compute_delivery_status', store=True)

    @api.depends('picking_ids', 'picking_ids.state')
    def _compute_delivery_status(self):
        for order in self:
            if not order.picking_ids or all(p.state == 'cancel' for p in order.picking_ids):
                order.delivery_status = False
            elif all(p.state in ['done', 'cancel'] for p in order.picking_ids):
                order.delivery_status = 'full'
            elif any(p.state == 'done' for p in order.picking_ids):
                order.delivery_status = 'partial'
            else:
                order.delivery_status = 'pending'
