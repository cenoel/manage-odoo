# -*- coding: utf-8 -*-

from odoo import models, fields, api

class ProductTemplate(models.Model):
    _inherit = 'product.template'

    is_machine_or_accessory = fields.Selection([
    		('is_machine','Is machine'),
    		('is_accessory','Is accessory'),
    		('othes','Others'),
    	],default='is_machine',string='Is machine or accessory')