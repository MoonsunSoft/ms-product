from odoo import fields, models, api


class ProductTemplate(models.Model):
    _inherit = "product.template"

    pricelist_product_template_ids = fields.One2many(
        "product.pricelist.item",
        "product_tmpl_id",
        compute="_compute_pricelist_product_template_ids",
        string="Price List"
    )

    @api.depends('product_variant_ids')
    def _compute_pricelist_product_template_ids(self):
        for product in self:
            product.pricelist_product_template_ids = self.env['product.pricelist.item'].search([
                '&',
                '|',
                ('product_tmpl_id', '=', product.id),
                ('product_id', 'in', product.product_variant_ids.ids),
                ('pricelist_id.active', '=', True),
            ])
            if product.pricelist_product_template_ids:
                price = product.compute_price(
                    product.id, product.pricelist_product_template_ids[0])
                print(price)

    @api.model
    def compute_price(self, product_id, pricelist_id, quantity=1):
        product = self.env['product.product'].browse(product_id)
        pricelist = self.env['product.pricelist'].browse(pricelist_id)
        if pricelist:
            price = pricelist.get_product_price(
                product, quantity, self.env.user.partner_id)
        else:
            price = product.lst_price
        return price


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
                '|',
                '&',
                ('product_tmpl_id', '=', product.product_tmpl_id.id),
                ('product_id', '=', False),
                '&',
                ('product_tmpl_id', '=', product.product_tmpl_id.id),
                ('product_id', '=', product.id),
                '&',
                ('product_tmpl_id', '=', False),
                ('product_id', '=', product.id),
            ])
