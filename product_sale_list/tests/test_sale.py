from odoo.tests import tagged
from odoo.tests.common import TransactionCase

@tagged("vw")
class productSaleListTest(TransactionCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()

    def test_saleehave(self):
        sale_lines = self.env["sale.order.line"]
        product = self.env["product.product"]
        product_template = self.env["product.template"]
        
        all_products = product.search([]).filtered(lambda x:x.sale_order_product_product_line_ids)
        for product in all_products:
            a = sale_lines.search([("state","=","sale"),("product_id","=",product.id)])
            b = product.sale_order_product_product_line_ids
            self.assertEqual(a,b)
        
        
        all_product_template = product_template.search([]).filtered(lambda x:x.sale_order_product_template_line_ids)
        for product in all_product_template:
            a = sale_lines.search([("state","=","sale"),("product_template_id","=",product.id)])
            b = product.sale_order_product_template_line_ids
            self.assertEqual(a,b)