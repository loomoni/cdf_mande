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


    name = fields.Char(string="Title", required=True)
    situation = fields.Char(string="Situation", required=False)
    changes = fields.Char(string="changes ", required=False)
    focus = fields.Selection([
        ('individual ', 'Individual '),
        ('household', 'Household'),
        ('community ', 'Community '),
    ], string="Focus ", default='individual', required=False)
    analysis = fields.Text(string="Analysis  ", required=False)
    lesson = fields.Text(string="Lesson learnt and recommendations  ", required=False)
    prepared_by = fields.Many2one(comodel_name='res.users', string="Prepared by", required=True)
    related_KRA = fields.Many2many(comodel_name='key.result.area', string="related KRA", )
    sp_outcome = fields.Many2many(comodel_name='key.result.area.outcomes.lines', string="SP Outcome", )
    project_outcome = fields.Many2many(comodel_name='program.project.outcomes.lines', string="Project Outcome", )
    description = fields.Html(string="Case Study Description", )
