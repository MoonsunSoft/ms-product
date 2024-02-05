from odoo.tests import tagged
from odoo.tests.common import TransactionCase

@tagged("vw")
class productPurchaseListTest(TransactionCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()

    def test_purchasehave(self):
        purchase_lines = self.env["purchase.order.line"]
        product = self.env["product.product"]
        product_template = self.env["product.template"]
        
        all_products = product.search([]).filtered(lambda x:x.purchase_order_product_product_line_ids)
        for product in all_products:
            a = purchase_lines.search([("state","=","purchase"),("product_id","=",product.id)])
            b = product.purchase_order_product_product_line_ids
            self.assertEqual(a,b)
        
        
        all_product_template = product_template.search([]).filtered(lambda x:x.purchase_order_product_template_line_ids)
        for product in all_product_template:
            a = purchase_lines.search([("state","=","purchase"),("product_template_id","=",product.id)])
            b = product.purchase_order_product_template_line_ids
            self.assertEqual(a,b)