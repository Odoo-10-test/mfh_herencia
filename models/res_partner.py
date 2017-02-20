# -*- coding: utf-8 -*-
from odoo import fields, models, api, _
from datetime import datetime

class ResPartnerInherit(models.Model):
    _inherit = 'res.partner'
    # campos basisos
    rut = fields.Char('RUT', size=14,help="Número de Documento de Identidad RUT")
    mail = fields.Char('Mail', size=100,help="Correo")
