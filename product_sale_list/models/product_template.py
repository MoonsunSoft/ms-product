from odoo import fields, models


class ProductTemplate(models.Model):
    _inherit = "product.template"

    sale_order_product_template_line_ids = fields.One2many(
        "sale.order.line",
        "product_template_id",
        string="Sale Order Lines",
        domain=[("state", "=", "sale")]
    )

class ProductProduct(models.Model):
    _inherit = "product.product"

    sale_order_product_product_line_ids = fields.One2many(
        "sale.order.line",
        "product_id",
        string="Sale Order Lines",
        domain=[("state", "=", "sale")],
    )


class SaleOrderLine(models.Model):
    _inherit = "sale.order.line"

    order_date = fields.Datetime(related="order_id.date_order")
