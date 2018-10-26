# -*- coding: utf-8 -*-

from odoo import api, models, _, fields


class StockPicking(models.Model):
    _inherit = "stock.picking"


    type_internal_transfert = fields.Selection([
        ('attach_or_detach','Attachment or Detachment'),
        ('natif','Natif')
    ],default='natif', string='Type of internal transfert')
