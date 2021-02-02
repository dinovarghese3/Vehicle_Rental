# -*- coding: utf-8 -*-
from odoo import fields, models


class ProductVideo(models.Model):
    _inherit = 'product.product'

    product_video = fields.Char(string="Product Video")
