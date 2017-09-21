# -*- coding: utf-8 -*-

from openerp import addons
from openerp import models, fields, api, _
from openerp.exceptions import UserError, RedirectWarning, ValidationError


class sale_order(models.Model):
	_inherit = ['sale.order']

	client_order_ref = fields.Char(string='Customer Reference', copy=False, required=True)

	@api.multi
	def action_confirm(self):	
		if self.env['sale.order'].search([('partner_id', '=', self.partner_id.id),\
			('client_order_ref', '=', self.client_order_ref),\
			('state', '!=', self.state)]):
			raise ValidationError(_('La referencia ya se ha usado para este cliente.'))
		else:
			return super(sale_order,self).action_confirm()