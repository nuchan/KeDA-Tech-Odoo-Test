
from odoo import api, fields, models
from odoo.exceptions import ValidationError


class MaterialRegistration(models.Model):
    _name = "material.registration"
    _description = "Material Registration"

    name = fields.Char('Material Name', required=True)
    code = fields.Char('Material Code', required=True)
    type = fields.Selection([('fabric', 'Fabric'),
                        ('jeans', 'Jeans'),
                        ('cotton', 'Cotton')], string='Material Type', required=True)
    price = fields.Float('Material Buy Price')
    supplier_id = fields.Many2one('res.partner', 'Supplier', required=True)

    @api.constrains('price')
    def check_price(self):
        for rec in self:
            if rec.price < 100:
                raise ValidationError('Material Buy Price cannot less than 100')