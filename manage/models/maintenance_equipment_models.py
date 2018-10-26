# -*- coding: utf-8 -*-

from odoo import models, fields, api


class MaintenanceEquipment(models.Model):
    _inherit = 'maintenance.equipment'

    @api.model
    def _default_removal_strategy_id(self):
        res = self.env['product.removal'].search([('name', 'like', 'FIFO')], limit=1)
        return res

    product_template_id = fields.Many2one('product.template', 'Linked product')
    is_machine_or_accessory = fields.Selection([
        ('is_machine', 'Is machine'),
        ('is_accessory', 'Is accessory'),
        ('othes', 'Others'),
    ], default='is_machine', string='Is machine or accessory')
    state = fields.Selection([
        ('available', 'Available'),
        ('patient', 'Patient'),
        ('unavailable', 'Unavailable')], default='available', string='State')
    lot_id = fields.Many2one('stock.production.lot', string='Lot name')
    location_id = fields.Many2one('stock.location', string='Location')
    removal_strategy_id = fields.Many2one('product.removal', 'Removal Strategy',
                                          default=_default_removal_strategy_id,
                                          help="Defines the default method used for suggesting the exact location (shelf) where to take the products from, which lot etc. for this location."
                                               " This method can be enforced at the product category level, and a fallback is made on the parent locations if none is set here.")


