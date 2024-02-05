from odoo import fields, models


class ProductTemplate(models.Model):
    _inherit = "product.template"
    # this is purchase lines for product_templates
    purchase_order_product_template_line_ids = fields.One2many(
        "purchase.order.line",
        "product_template_id",
        string="Purchase Order Lines",
        domain=[("state", "=", "purchase")]
    )


class ProductProduct(models.Model):
    _inherit = "product.product"

    purchase_order_product_product_line_ids = fields.One2many(
        "purchase.order.line",
        "product_id",
        string="Purchase Order Lines",
        domain=[("state", "=", "purchase")],
    )
