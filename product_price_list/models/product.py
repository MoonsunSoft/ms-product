from odoo import fields, models, api

class ProductTemplate(models.Model):
    _inherit = "product.template"

    pricelist_product_template_ids = fields.One2many(
        "product.pricelist.item",
        "product_tmpl_id",
        domain=lambda self: [
            '&',
                '|', 
                ('product_tmpl_id', '=', self.id), 
                ('product_id', 'in', self.product_variant_ids.ids),
            ('pricelist_id.active', '=', True),
        ],
        string="Price List"
    )


class ProductProduct(models.Model):
    _inherit = "product.product"

    pricelist_product_product_ids = fields.One2many(
        "product.pricelist.item",
        "product_id",
        compute="_compute_pricelist_product_ids",
        string="Price List"
    )

    @api.depends('product_tmpl_id')
    def _compute_pricelist_product_ids(self):
        for product in self:
            product.pricelist_product_product_ids = self.env['product.pricelist.item'].search([
                ('pricelist_id.active', '=', True),
                '|',
                    '&',
                    ('product_tmpl_id', '=', product.product_tmpl_id.id),
                    ('product_id', '=', False),
                    '&',
                    ('product_tmpl_id', '=', product.product_tmpl_id.id),
                    ('product_id', '=', product.id),
            ])
