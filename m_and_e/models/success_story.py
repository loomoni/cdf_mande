from odoo import models, fields, api, _

date_format = "%Y-%m-%d"


class SuccessStory(models.Model):
    _name = 'success.story'
    _inherit = ['mail.thread', 'mail.activity.mixin']


    state = fields.Selection([
        ('draft', 'Draft'),
        ('reported', 'Reported'),
        ('review', 'Program Manager Reviewed'),
        ('head_of_operation_review', 'Head of Operations Reviewed'),
        ('approve', 'Executive Director Approved'),
        ('reject', 'Rejected'),
    ],
        string="Status", default='draft',
        track_visibility='onchange', )

    @api.multi
    def button_reported(self):
        self.write({'state': 'reported'})
        return True

    @api.multi
    def button_supervisor_review(self):
        self.write({'state': 'review'})
        return True

    @api.multi
    def back_to_draft(self):
        self.write({'state': 'draft'})
        return True

    @api.multi
    def button_program_review(self):
        self.write({'state': 'head_of_operation_review'})
        return True

    @api.multi
    def button_program_manager_back_to_supervisor(self):
        self.write({'state': 'reported'})
        return True

    @api.multi
    def button_approve(self):
        self.write({'state': 'approve'})
        return True

    name = fields.Char(string="Story Title", required=True)
    site = fields.Char(string="Site", required=False)
    prepared_by = fields.Many2one(comodel_name='res.users', string="Prepared by", required=True)
    description = fields.Html(string="Story Description",)
