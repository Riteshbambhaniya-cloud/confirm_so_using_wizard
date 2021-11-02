# -*- coding: utf-8 -*-

from odoo import models, fields, api


class ResCompany(models.Model):
    _inherit = 'res.company'
    _description = 'res company inherit'

    @api.model
    def create(self,vals):
        dept_obj = self.env['hr.department']
        res = super(ResCompany, self).create(vals)
        dept_obj.sudo().create(
            {'name':res.name,
             'company_id':res.id})
        return res
