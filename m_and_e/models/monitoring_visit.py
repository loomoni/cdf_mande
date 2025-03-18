from odoo import models, fields, api


class MonitoringVisitReport(models.Model):
    _name = 'monitoring.visit.report'
    _description = 'Monitoring Visit Report'

    name = fields.Char(string="Name", required=True)
    attachment = fields.Binary(string="Attachment", attachment=True, store=True, )
    attachment_file_name = fields.Char(string="Attachment file")
    url = fields.Char(string="URL")
    type = fields.Selection([('binary', 'File'),
                             ('url', 'URL')], default='binary', string="Type")
