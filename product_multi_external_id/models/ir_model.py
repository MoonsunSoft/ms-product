from odoo import fields, models, _
import logging
_logger = logging.getLogger(__name__)


class IrModelData(models.Model):
    """Holds external identifier keys for records in the database.
       This has two main uses:

           * allows easy data integration with third-party systems,
             making import/export/sync of data possible, as records
             can be uniquely identified across multiple systems
           * allows tracking the origin of data installed by Odoo
             modules themselves, thus making it possible to later
             update them seamlessly.
    """
    _inherit = 'ir.model.data'

    partner_id = fields.Many2one('res.partner', string='partner_id')
