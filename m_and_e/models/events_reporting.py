from odoo import models, fields, api, _

date_format = "%Y-%m-%d"


class EventReporting(models.Model):
    _name = 'event.reporting'
    _description = 'This table handle all the event reported'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _rec_name = 'event_type'

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

    achievements_reporting_lines = fields.One2many(comodel_name="event.result.achievement",
                                                   inverse_name="achievements_reporting_id",
                                                   string="Achievement IDs", required=False, )

    achievements_output_reporting_lines = fields.One2many(comodel_name="event.result.output.achievement",
                                                          inverse_name="achievements_output_reporting_id",
                                                          string="Achievement IDs", required=False, )


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

    outcome_output_indicator = fields.Many2one(comodel_name='program.project.outcome.indicators', string='Outcome Indicator')
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

    outcome_output_indicator = fields.Many2one(comodel_name='program.project.output.indicators', string='Output Indicator')
    outcome_unit_definition = fields.Many2one(comodel_name='program.project.output.unit.definition', string='Unit/Definition')
    outcome_year = fields.Many2one(comodel_name='program.project.output.actual.period.lines', string='Year')
    outcome_actual_period = fields.Many2one(comodel_name='program.project.output.actual.period.section.lines', string='Period')
    actual_value = fields.Integer(string='Value')
    achievements_output_reporting_id = fields.Many2one(comodel_name='event.reporting', string='Achievement')

