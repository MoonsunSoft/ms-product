# -*- coding: utf-8 -*-
# Part of BrowseInfo. See LICENSE file for full copyright and licensing details.

from odoo import fields, models, api, _


class PosConfig(models.Model):
	_inherit = "pos.config"

	allow_product_variants = fields.Boolean(string="Allow Product Variants")
	allow_alternative_products = fields.Boolean(string="Allow Alternative Product Variants")
	allow_selected_close = fields.Selection(
		[('auto_close', 'Allow Auto Close Popup'), ('selected', 'Allow Selected Popup Does not close Popup')],
		string="Allow Selected From Popup", default="auto_close")


class ResConfigSettings(models.TransientModel):
	_inherit = 'res.config.settings'

	allow_product_variants = fields.Boolean(related='pos_config_id.allow_product_variants',readonly=False)
	allow_alternative_products = fields.Boolean(related='pos_config_id.allow_alternative_products',readonly=False)
	allow_selected_close = fields.Selection(related='pos_config_id.allow_selected_close',readonly=False)


class ProductTemp(models.Model):
	_inherit = 'product.template'

	product_ids = fields.Many2many('product.product', string='Alternative Products',
								   domain=[('available_in_pos', '=', True)])

class Product(models.Model):
	_inherit = 'product.product'

	template_name=fields.Char(string="tempalte name")


class POSSession(models.Model):
	_inherit = 'pos.session'

	def _loader_params_product_product(self):
		res = super(POSSession, self)._loader_params_product_product()
		fields = res.get('search_params').get('fields')
		fields.extend(['product_template_attribute_value_ids','product_ids','product_variant_count','name'])
		res['search_params']['fields'] = fields
		return res

	def _pos_ui_models_to_load(self):
		result = super()._pos_ui_models_to_load()
		new_model = 'product.template'
		if new_model not in result:
			result.append(new_model)
		return result

	def _loader_params_product_template(self):
		return {'search_params': {'domain': [('sale_ok','=',True),('available_in_pos','=',True)], 'fields': ['name','display_name','product_variant_ids','product_variant_count','product_ids']}}

	def _get_pos_ui_product_template(self, params):
		return self.env['product.template'].search_read(**params['search_params'])
