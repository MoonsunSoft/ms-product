from odoo import api, fields, models, _

class PurchaseOrderLine(models.Model):
    _inherit = "purchase.order.line"

    product_template_id = fields.Many2one(
        "product.template", 
        string="Product",
        compute='_compute_product_template_id',
        readonly=False,
        search='_search_product_template_id',)

    @api.depends("product_id")
    def _compute_product_template_id(self):
        for line in self:
            line.product_template_id = line.product_id.product_tmpl_id
            
    def _search_product_template_id(self, operator, value):
        return [('product_id.product_tmpl_id', operator, value)]
