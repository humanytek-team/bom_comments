from openerp import api, fields, models


class BoMComments(models.Model):
    _inherit = 'mrp.bom.line'

    general_comments = fields.Text()
    production_comments = fields.Text()
