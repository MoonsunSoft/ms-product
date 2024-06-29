from odoo import models, _, api, fields


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    def action_view_external_ids(self):
        self.ensure_one()
        ctx = dict(
            create=True,
            default_res_id=self.id,
            default_model=self._name,
            default_module="product"
        )
        action = {
            'name': _("External Ids Product"),
            'type': 'ir.actions.act_window',
            'res_model': 'ir.model.data',
            'target': 'current',
            'context': ctx
        }
        external_ids = self.env['ir.model.data'].search(
            [('res_id', '=', self.id), ('model', '=', self._name)])
        ext_ids = []
        for each in external_ids:
            ext_ids.append(each.id)
        if len(ext_ids) == 1:
            service_id = ext_ids and ext_ids[0]
            action['res_id'] = service_id
            action['view_mode'] = 'form'
            action['views'] = [
                (self.env.ref('base.view_model_data_form').id, 'form')]
        else:
            action['view_mode'] = 'tree,form'
            action['domain'] = [('id', 'in', ext_ids)]
        return action


class ProductProduct(models.Model):
    _inherit = 'product.product'

    def action_view_external_ids(self):
        self.ensure_one()
        ctx = dict(
            create=True,
            default_res_id=self.id,
            default_model=self._name,
            default_module="product"
        )
        action = {
            'name': _("External Ids Product"),
            'type': 'ir.actions.act_window',
            'res_model': 'ir.model.data',
            'target': 'current',
            'context': ctx
        }
        external_ids = self.env['ir.model.data'].search(
            [('res_id', '=', self.id), ('model', '=', self._name)])
        ext_ids = []
        for each in external_ids:
            ext_ids.append(each.id)
        if len(ext_ids) == 1:
            service_id = ext_ids and ext_ids[0]
            action['res_id'] = service_id
            action['view_mode'] = 'form'
            action['views'] = [
                (self.env.ref('base.view_model_data_form').id, 'form')]
        else:
            action['view_mode'] = 'tree,form'
            action['domain'] = [('id', 'in', ext_ids)]
        return action
