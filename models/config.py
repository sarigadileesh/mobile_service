from odoo import models, fields, api


class mobile_service1(models.Model):
    _name = 'mobile_service.config1'
    _description = 'configuration model report'

    brandname = fields.Many2one('res.partner', string='Mobile Brand')
    model1 = fields.Many2one('res.partner', string='Model Name')

class mobile_service2(models.Model):
    _name = 'mobile_service.config2'
    _description = 'configuration complaint report'

    comptemp = fields.Char('Complaint Type Template')
    compdes = fields.Char('Complaint Description')

class mobile_service3(models.Model):
    _name = 'mobile_service.config3'
    _description = 'configuration complaint type report'

    comptype = fields.Char('Complaint Type')

class mobile_service4(models.Model):
    _name = 'mob.config4'
    _description = 'configuration terms and conditions report'

    terms1 = fields.Text('Terms and Conditions')