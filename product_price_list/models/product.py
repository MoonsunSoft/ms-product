from odoo import fields, models

class ProductTemplate(models.Model):
    _inherit = "product.template"

    pricelist_product_template_ids = fields.One2many(
        "product.pricelist.item",
        "product_tmpl_id",
        string="Price List"
    )


class ProductProduct(models.Model):
    _inherit = "product.product"

    pricelist_product_product_ids = fields.One2many(
        "product.pricelist.item",
        "product_id",
        string="Price List"
    )
