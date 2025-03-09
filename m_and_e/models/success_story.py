from odoo import models, fields, api, _

date_format = "%Y-%m-%d"


class SuccessStory(models.Model):
    _name = 'success.story'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string="Story Title", required=True)
    site = fields.Char(string="Site", required=False)
    prepared_by = fields.Many2one(comodel_name='res.users', string="Prepared by", required=True)
    description = fields.Html(string="Story Description",)
