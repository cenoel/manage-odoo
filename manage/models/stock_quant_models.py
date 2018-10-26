# -*- coding: utf-8 -*-

from odoo import models, fields, api,_
from odoo.exceptions import UserError

class StockQuant(models.Model):
    _inherit = "stock.quant"

    @api.model
    def create(self, values):
        quant_created_ref = super(StockQuant, self).create(values)
        ckeck_quant = self.env['stock.quant'].search([('id', '=', quant_created_ref.id)])
        equipment_ref = self.env['maintenance.equipment']
        new_quantity = 0
        if ckeck_quant.id == True:
            new_quantity = quant_created_ref.quantity - ckeck_quant.quantity
        else:
            new_quantity = quant_created_ref.quantity
        picking_search_ref = self.env['stock.picking'].search([('create_uid', '=', self.env.user.id)],order='id desc', limit=1)
        self._update_and_create_accessory_machine(picking_search_ref, new_quantity, equipment_ref, quant_created_ref)


    @api.multi
    def write(self, values):
        equipment_ref = self.env['maintenance.equipment']
        quant_ref = self.env['stock.quant'].search([('id', '=', self.id)])
        new_quantity = 0
        old_quantity = self.quantity
        write_ref = super(StockQuant, self).write(values)
        quant_stock_ref = self.env['stock.quant'].search([('id', '=', self.id)])
        new_value_quantity = values.get('quantity')
        new_quantity = new_value_quantity - old_quantity
        picking_search_ref = self.env['stock.picking'].search([('create_uid', '=', self.env.user.id)], order='id desc',
                                                              limit=1)
        self._update_and_create_accessory_machine(picking_search_ref, new_quantity, equipment_ref, self)

        return quant_stock_ref

    def _update_and_create_accessory_machine(self, picking_search_ref, new_quantity, equipment_ref , quant_ref):
        if picking_search_ref.picking_type_id.code == 'incoming':
            if quant_ref.location_id.id != self.env.ref('stock.stock_location_suppliers').id:
                count_iteration_picking = 0
                while count_iteration_picking < new_quantity:
                    data_to_create = {
                        'name': quant_ref.product_id.product_tmpl_id.name,
                        'product_template_id': quant_ref.product_id.product_tmpl_id.id,
                        'is_machine_or_accessory': quant_ref.product_id.product_tmpl_id.is_machine_or_accessory,
                        'lot_id': quant_ref.lot_id.id,
                        'location_id': quant_ref.location_id.id,
                    }
                    equipment_ref.create(data_to_create)
                    count_iteration_picking += 1

        if picking_search_ref.picking_type_id.code == 'internal':
            count_iteration_picking = 0
            while count_iteration_picking < new_quantity:
                if picking_search_ref.type_internal_transfert == 'natif':
                    equipment_transfert_ref = equipment_ref.search([
                        ('product_template_id', '=', self.product_id.product_tmpl_id.id),
                        ('state', '=', 'available'),
                        ('lot_id', '=', quant_ref.lot_id.id),
                        ('location_id', '=', picking_search_ref.location_id.id)
                    ])
                    data_to_update = {
                        'state': 'available',
                        'location_id': quant_ref.location_id.id
                    }
                    equipment_transfert_ref.update(data_to_update)
                count_iteration_picking += 1
