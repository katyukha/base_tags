# -*- coding: utf-8 -*-
from openerp.osv import orm


class SaleOrder(orm.Model):
    _name = "sale.order"
    _inherit = ["sale.order",
                "res.tag.mixin"]


class SaleOrderLine(orm.Model):
    _name = "sale.order.line"
    _inherit = ["sale.order.line",
                "res.tag.mixin"]
