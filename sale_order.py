# -*- coding: utf-8 -*-

from openerp import addons
from openerp import models, fields, api, _
from openerp.exceptions import UserError, RedirectWarning, ValidationError


class sale_order(models.Model):
	_inherit = ['sale.order']

	client_order_ref = fields.Char(string='Customer Reference', copy=False, required=True)

	# @api.multi
	# def action_confirm(self):
	#   if self.env['sale.order'].search([('partner_id', '=', self.partner_id.id),\
	#       ('client_order_ref', '=', self.client_order_ref),\
	#       ('state', '!=', self.state)]):
	#       raise ValidationError(_('La referencia ya se ha usado para este cliente.'))
	#   #else:
	#       return super(sale_order,self).action_confirm()  


	@api.onchange('client_order_ref')
	def _onchange_client_order_ref(self):
		if self.env['sale.order'].search([('partner_id', '=', self.partner_id.id),\
			('client_order_ref', '=', self.client_order_ref),\
			('state', '!=', self.state)]):
					warning_mess = {
						'title': _('ValidationError'),
						'message' : _('La referencia ya se ha usado para este cliente.')
					}
					return {'warning': warning_mess}
		return {}


		# return {
		#       'type': 'ir.actions.client',
		#       'tag': 'action_warn'
		#       'name': _('Aviso'),
		#       'context': context,
		#       'params' : {
		#           'title' : _('Aviso'),
		#           'text' : _('Referencia interna del cliente ya ha sido utilizada previamente.'),
		#           'sticky' : True
		#       }}
