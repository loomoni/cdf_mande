from odoo import models, fields, api, _

date_format = "%Y-%m-%d"


class CaseStudy(models.Model):
    _name = 'case.study'
    _description = 'This table handle all the case study'
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

    def button_reported(self):
        self.write({'state': 'reported'})
        return True

    def button_supervisor_review(self):
        self.write({'state': 'review'})
        return True

    def back_to_draft(self):
        self.write({'state': 'draft'})
        return True

    def button_program_review(self):
        self.write({'state': 'head_of_operation_review'})
        return True

    def button_program_manager_back_to_supervisor(self):
        self.write({'state': 'reported'})
        return True

    def button_approve(self):
        self.write({'state': 'approve'})
        return True

    name = fields.Char(string="Title", required=True)
    situation = fields.Html(string="Situation", required=False)
    changes = fields.Html(string="changes ", required=False)
    focus = fields.Selection([
        ('individual ', 'Individual '),
        ('household', 'Household'),
        ('community ', 'Community '),
    ], string="Focus ", default='individual', required=False)
    analysis = fields.Html(string="Analysis  ", required=False)
    lesson = fields.Html(string="Lesson learnt and recommendations  ", required=False)
    prepared_by = fields.Many2one(comodel_name='res.users', string="Prepared by", required=True)
    related_KRA = fields.Many2many(comodel_name='key.result.area', string="related KRA", )
    sp_outcome = fields.Many2many(comodel_name='key.result.area.outcomes.lines', string="SP Outcome", )
    project_outcome = fields.Many2many(comodel_name='program.project.outcomes.lines', string="Project Outcome", )
    description = fields.Html(string="Case Study Description", )
