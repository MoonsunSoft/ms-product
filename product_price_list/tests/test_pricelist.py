from odoo.tests import tagged
from odoo.fields import Command
from odoo.tests.common import TransactionCase


@tagged("vw")
class productPriceListTest(TransactionCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()

    def test_pricelisthave(self):
        peice_list = self.env["product.pricelist.item"]
        product = self.env["product.product"]
        product_template = self.env["product.template"]

        all_products = product.search([])
        all_product_template = product_template.search([])

        pricelist = self.env["product.pricelist"].create(
            {
                "name": "Test Pricelist",
                "currency_id": self.env.ref("base.EUR").id,
            }
        )

        all_products[0].list_price = 100.0
        all_products[1].list_price = 100.0
        all_product_template[0].list_price = 100.0

        self.env["product.pricelist"].create(
            {
                "name": "Foo",
                "item_ids": [
                    Command.create(
                        {"product_id": all_products[0].id, "fixed_price": 1}
                    ),
                    Command.create(
                        {"product_id": all_products[1].id, "fixed_price": 1}
                    ),
                    Command.create(
                        {
                            "product_tmpl_id": all_product_template[0].id,
                            "fixed_price": 1,
                        }
                    ),
                ],
            }
        )

        self.env["product.pricelist"].create(
            {
                "name": "Foo1",
                "item_ids": [
                    Command.create(
                        {"product_id": all_products[0].id, "fixed_price": 1}
                    ),
                    Command.create(
                        {
                            "product_tmpl_id": all_product_template[0].id,
                            "fixed_price": 1,
                        }
                    ),
                ],
            }
        )

        all_products = product.search([]).filtered(
            lambda x: x.pricelist_product_product_ids
        )
        for product in all_products:
            a = peice_list.search([("product_id", "=", product.id)])
            b = product.pricelist_product_product_ids
            self.assertEqual(a, b)

        all_product_template = product_template.search([]).filtered(
            lambda x: x.pricelist_product_template_ids
        )
        for product in all_product_template:
            a = peice_list.search([("product_tmpl_id", "=", product.id)])
            b = product.pricelist_product_template_ids
            self.assertEqual(a, b)
