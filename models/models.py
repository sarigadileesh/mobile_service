# -*- coding: utf-8 -*-

from odoo import models, fields, api, _


class mobile_service(models.Model):
    _name = 'mobile_service.service_request'
    _description = 'service_request report'

    # name = fields.Many2one('res.user', string='Customer Name',required=True)
    name = fields.Char('Customer Name',required=True)
    num = fields.Integer('Contact Number')
    email = fields.Char('Email')
    address = fields.Char()
    brname = fields.Char(string='Brand Name')
    model = fields.Char(string='Model Name')
    date1 = fields.Date('Requested date')
    date2 = fields.Date('Return date',required=True)
    sfield = fields.Selection([
        ('Draft', 'Draft'),
        ('Returned', 'Returned'),
        ('Not solved', 'Not solved')
    ], default='Draft')
    tick1 = fields.Boolean('In Warranty')
    tick2 = fields.Boolean('Re-repair')
    imei = fields.Char(string='IMEI Number')
    notes = fields.Char('Internal notes')
    tech = fields.Many2one('res.partner', string="Technician Name", required=True)
    complaint_ids = fields.One2many('mobile_service.complaints','num')
    partsusage_ids = fields.One2many('mobile_service.partsusage','email')

    def action_assign(self):
        for rec in self:
            rec.sfield = 'Returned'

    def action_print(self):
        for rec in self:
            rec.sfield = 'Not solved'

    mob_seq = fields.Char(string='Request No.', required=True,
                           copy=False, readonly=True, index=True, default=lambda self: _('New'))

    @api.model
    def create(self, vals):
        if vals.get('mob_seq', _('New')) == _('New'):
            vals['mob_seq'] = self.env['ir.sequence'].next_by_code('mobileserv_seq') or _('New')
        result = super(mobile_service, self).create(vals)
        return result

class complaints(models.Model):
    _name = 'mobile_service.complaints'
    _description = 'complaints report'

    category123 = fields.Char(string='Category')
    desp123 = fields.Char(string='Description')
    num = fields.Many2one('phone_shop.service_request',string='numm')

class partsusage(models.Model):
    _name = 'mobile_service.partsusage'
    _description = 'Parts usage report'

    prod = fields.Char(string='Product')
    usedquan = fields.Integer(string='Used Quantity')
    unit = fields.Char(string='Unit of measure')
    unprice = fields.Char(string='Unit Price')
    stock = fields.Char(string='Stock Movement')
    invoicedq = fields.Char(string='Invoiced qt')
    price = fields.Char(string='Price')
    email = fields.Many2one('phone_shop.service_request', string='emaill')


