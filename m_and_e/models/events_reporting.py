from odoo import models, fields, api, _

date_format = "%Y-%m-%d"


class EventReporting(models.Model):
    _name = 'event.reporting'
    _description = 'This table handle all the event reported'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _rec_name = 'event_type'

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

    def button_back_to_program_manager(self):
        self.write({'state': 'review'})
        return True

    def button_reject(self):
        self.write({'state': 'reject'})
        return True

    @api.onchange('region')
    def _onchange_region_id(self):
        sections = []
        for section in self.region:
            sections.append(section.id)
        return {'domain': {'district': [('district_id', 'in', sections)]}}

    # General Information
    event_type = fields.Char(string="Event type", required=True)
    venue = fields.Char(string="Venue", required=False, )
    partner = fields.Char(string="Partner", required=False, )
    conduct_by = fields.Many2one(comodel_name="res.users", string="Conducted by", required=False, )
    event_date_start = fields.Datetime(string="Event Starting Date & time")
    event_date_closing = fields.Datetime(string="Event Closing Date & time")
    reported_for = fields.Char(string="Reported For")
    reporting_date = fields.Date(string="Reporting date")

    # Reporter section
    event_coordinator = fields.Char(string="Event Coordinator")
    title = fields.Char(string="Title")
    region = fields.Many2one(comodel_name="region", string="Region")
    district = fields.Many2one(comodel_name="district.lines", string="District")
    ward = fields.Char(string="Ward")
    project_name = fields.Many2one(comodel_name="program.project", string="Project Name")

    # Objective / s of the event
    introducation = fields.Text(string="Introduction")
    overall_objectives = fields.Text(string="Overall objective of the activity/event")
    specific_objectives = fields.Text(string="Specific objectives of the activity/even")
    strategic_plan = fields.Many2many(comodel_name="key.result.area", string="SP")
    # output = fields.Char(string="Output")
    sp_indicators = fields.Many2one(comodel_name="kra.outcome.indicators", string="Indicator")
    # contribution_to_sdg = fields.Many2many(comodel_name="sdg.configuration", string="Contributing to SDG")

    description_of_the_event = fields.Html(string="Description")
    achievements = fields.Text(string="Achievements Description")
    other_resource_utilized = fields.Char(string="Other resource utilised")
    challenges_encountered = fields.Text(string="Challenges encountered")
    lesson_learned = fields.Text(string="Lesson learned")
    way_forward = fields.Text(string="Way forward")
    unexpected_result = fields.Text(string="Unexpected/Unintended Result")

    # Budget section
    activity_addressed = fields.Many2one(comodel_name="project.activity", string="Activity addressed")
    # budget_code = fields.Char(string="Budget Code")
    currency_id = fields.Many2one("res.currency", string="Currency", required=False,
                                  related='activity_addressed.currency_id')
    budget = fields.Monetary(string="Planed Budget", related='activity_addressed.budget')
    budget_description_line_ids = fields.One2many(comodel_name="budget.utilized",
                                                  inverse_name="budget_description_id",
                                                  string="Budget IDs", required=False, )
    actual_budget = fields.Monetary(string="Actual Budget", compute='actual_budget_compute')
    balance = fields.Monetary(string="Balance", compute='balance_compute')

    achievements_reporting_lines = fields.One2many(comodel_name="event.result.achievement",
                                                   inverse_name="achievements_reporting_id",
                                                   string="Achievement IDs", required=False, )

    achievements_output_reporting_lines = fields.One2many(comodel_name="event.result.output.achievement",
                                                          inverse_name="achievements_output_reporting_id",
                                                          string="Achievement IDs", required=False, )

    event_attachment_files_lines = fields.One2many(comodel_name="event.attachment.files",
                                                   inverse_name="event_attachment_id",
                                                   string="Attachment IDs", required=False, )

    @api.depends('budget', 'actual_budget')
    def balance_compute(self):
        for rec in self:
            rec.balance = rec.budget - rec.actual_budget

    @api.depends('budget_description_line_ids.cost')
    def actual_budget_compute(self):
        for rec in self:
            rec.actual_budget = 0 + sum(line.cost for line in rec.budget_description_line_ids)


class EventResultAchievement(models.Model):
    _name = 'event.result.achievement'
    _description = 'All result achievement are stored in this table'

    @api.onchange('outcome_output_indicator')
    def _onchange_outcome_output_indicator_id(self):
        sections = []
        for section in self.outcome_output_indicator:
            sections.append(section.id)
        return {'domain': {'outcome_unit_definition': [('unit_definition_line', 'in', sections)]}}

    @api.onchange('outcome_unit_definition')
    def _onchange_outcome_unit_definition_id(self):
        sections = []
        for section in self.outcome_unit_definition:
            sections.append(section.id)
        return {'domain': {'outcome_year': [('unit_line_id', 'in', sections)]}}

    @api.onchange('outcome_year')
    def _onchange_outcome_year_id(self):
        sections = []
        for section in self.outcome_year:
            sections.append(section.id)
        return {'domain': {'outcome_actual_period': [('actual_period_section_line', 'in', sections)]}}

    outcome_output_indicator = fields.Many2one(comodel_name='program.project.outcome.indicators',
                                               string='Outcome Indicator')
    output_indicator = fields.Many2one(comodel_name='program.project.output.indicators', string='Outcome')
    outcome_unit_definition = fields.Many2one(comodel_name='program.project.unit.definition', string='Unit'
                                                                                                     '/Definition')
    outcome_year = fields.Many2one(comodel_name='program.project.actual.period.lines', string='Year')
    actual_value_year = fields.Integer(string='Year Target', related="outcome_year.target_value")
    outcome_actual_period = fields.Many2one(comodel_name='program.project.actual.period.section.lines', string='Period')
    section_actual_period = fields.Integer(string='Target Value', related='outcome_actual_period.target_value')
    arrived = fields.Integer(string='Arrived')
    actual_value = fields.Integer(string='Achievement')
    achievements_reporting_id = fields.Many2one(comodel_name='event.reporting', string='Achievement ID')
    gender = fields.Selection([('female', 'Female'), ('men', 'Men'), ], string="Gender")


class EventResultOutputAchievement(models.Model):
    _name = 'event.result.output.achievement'
    _description = 'All result achievement are stored in this table'

    @api.onchange('outcome_output_indicator')
    def _onchange_outcome_output_indicator_id(self):
        sections = []
        for section in self.outcome_output_indicator:
            sections.append(section.id)
        return {'domain': {'outcome_unit_definition': [('output_unit_definition_line', 'in', sections)]}}

    @api.onchange('outcome_unit_definition')
    def _onchange_outcome_unit_definition_id(self):
        sections = []
        for section in self.outcome_unit_definition:
            sections.append(section.id)
        return {'domain': {'outcome_year': [('output_unit_line_id', 'in', sections)]}}

    @api.onchange('outcome_year')
    def _onchange_outcome_year_id(self):
        sections = []
        for section in self.outcome_year:
            sections.append(section.id)
        return {'domain': {'outcome_actual_period': [('output_actual_period_section_line', 'in', sections)]}}

    outcome_output_indicator = fields.Many2one(comodel_name='program.project.output.indicators',
                                               string='Output Indicator')
    outcome_unit_definition = fields.Many2one(comodel_name='program.project.output.unit.definition',
                                              string='Unit/Definition')
    outcome_year = fields.Many2one(comodel_name='program.project.output.actual.period.lines', string='Year')
    outcome_actual_period = fields.Many2one(comodel_name='program.project.output.actual.period.section.lines',
                                            string='Period')
    actual_value = fields.Integer(string='Value')
    achievements_output_reporting_id = fields.Many2one(comodel_name='event.reporting', string='Achievement')


class BudgetUtilized(models.Model):
    _name = 'budget.utilized'
    _description = 'Table with the budget utilized'
    _rec_name = "item"

    item = fields.Char(string="Add Item Description")
    cost = fields.Float(string="Cost")
    budget_description_id = fields.Many2one(comodel_name="event.reporting", string="Budget ID",
                                            required=False, readonly=True)


class EventAttachmentFiles(models.Model):
    _name = 'event.attachment.files'
    _description = 'All result attachment'

    attachment = fields.Binary(string="Attachment", attachment=True, store=True, )
    attachment_name = fields.Char(string="Attachment Name")
    attachment_file_name = fields.Char(string="Attachment file")
    event_attachment_id = fields.Many2one("event.reporting", string="Attachment ID", required=False, )
