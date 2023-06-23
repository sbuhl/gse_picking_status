# -*- coding: utf-8 -*-

from odoo import api, fields, models
from odoo.tools import float_compare


class PurchaseOrder(models.Model):
    _inherit = "purchase.order"

    receipt_status = fields.Selection([
         ('pending', 'Not Received'),
         ('partial', 'Partially Received'),
         ('full', 'Fully Received'),
     ], string='Receipt Status', compute='_compute_receipt_status', store=True)

    @api.depends('picking_ids', 'picking_ids.state')
    def _compute_receipt_status(self):
        for order in self:
            if not order.picking_ids or all(p.state == 'cancel' for p in order.picking_ids):
                order.receipt_status = False
            elif all(p.state in ['done', 'cancel'] for p in order.picking_ids):
                if all(float_compare(line.qty_received, line.product_qty, precision_rounding=line.product_uom.rounding) >= 0 for line in order.order_line):
                    order.receipt_status = 'full'
                else:
                    order.receipt_status = 'partial'
            elif any(p.state == 'done' for p in order.picking_ids):
                order.receipt_status = 'partial'
            else:
                order.receipt_status = 'pending'
