from odoo import models, fields, api, _

date_format = "%Y-%m-%d"


class EventReporting(models.Model):
    _name = 'event.reporting'
    _description = 'This table handle all the event reported'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _rec_name = 'event_type'

    event_type = fields.Char(string="Event type", required=True)
