from odoo import models, fields, api, _

date_format = "%Y-%m-%d"


class MeIndicators(models.Model):
    _name = 'me.indicators'
    _description = 'region table'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _rec_name = 'indicators'

    indicators = fields.Text(string="Indicator", required=False, )
    indicator_area = fields.Many2many(comodel_name="district.lines", string="Area Applied", required=False, )

    @api.model
    def get_indicators(self):
        search_indicators = self.env['me.indicators'].search([])
        return {
            'total_indicators': len(search_indicators)
        }


# class EventReporting(models.Model):
#     _name = 'event.reporting'
#     _description = 'This table handle all the event reported'
#     _inherit = ['mail.thread', 'mail.activity.mixin']
#     _rec_name = 'event_type'
#
#     state = fields.Selection([
#         ('draft', 'Draft'),
#         ('reported', 'Reported'),
#         ('review', 'Program Manager Reviewed'),
#         ('head_of_operation_review', 'Head of Operations Reviewed'),
#         ('approve', 'Executive Director Approved'),
#         ('reject', 'Rejected'),
#     ],
#         string="Status", default='draft',
#         track_visibility='onchange', )
#
#     @api.multi
#     def button_reported(self):
#         self.write({'state': 'reported'})
#         return True
#
#     @api.multi
#     def button_supervisor_review(self):
#         self.write({'state': 'review'})
#         return True
#
#     @api.multi
#     def back_to_draft(self):
#         self.write({'state': 'draft'})
#         return True
#
#     @api.multi
#     def button_program_review(self):
#         self.write({'state': 'head_of_operation_review'})
#         return True
#
#     @api.multi
#     def button_program_manager_back_to_supervisor(self):
#         self.write({'state': 'reported'})
#         return True
#
#     @api.multi
#     def button_approve(self):
#         self.write({'state': 'approve'})
#         return True
#
#     @api.multi
#     def button_back_to_program_manager(self):
#         self.write({'state': 'review'})
#         return True
#
#     @api.multi
#     def button_reject(self):
#         self.write({'state': 'reject'})
#         return True
#
#     @api.onchange('region')
#     def _onchange_region_id(self):
#         sections = []
#         for section in self.region:
#             sections.append(section.id)
#         return {'domain': {'district': [('district_id', 'in', sections)]}}
#
#     # @api.onchange('project_name')
#     # def _onchange_project_name_id(self):
#     #     sections = []
#     #     for section in self.project_name:
#     #         sections.append(section.id)
#     #     return {'domain': {'activity_addressed': [('project_activities', 'in', sections)]}}
#
#     # General information
#     event_type = fields.Many2one(comodel_name="events.configuration", string="Event type", required=True, )
#     venue = fields.Char(string="Venue", required=False, )
#     partner = fields.Char(string="Partner", required=False, )
#     conduct_by = fields.Many2one(comodel_name="res.users", string="Conducted by", required=False, )
#     event_date_start = fields.Datetime(string="Event Starting Date & time")
#     event_date_closing = fields.Datetime(string="Event Closing Date & time")
#     reported_for = fields.Char(string="Reported For")
#     reporting_date = fields.Date(string="Reporting date")
#
#     # Reporter section
#     event_coordinator = fields.Char(string="Event Coordinator")
#     title = fields.Char(string="Title")
#     region = fields.Many2one(comodel_name="region", string="Region")
#     district = fields.Many2one(comodel_name="district.lines", string="District")
#     ward = fields.Char(string="Ward")
#     project_name = fields.Many2one(comodel_name="project.project", string="Project Name")
#
#     # Objective / s of the event
#     introducation = fields.Text(string="Introduction")
#     overall_objectives = fields.Text(string="Overall objective of the activity/event")
#     specific_objectives = fields.Text(string="Specific objectives of the activity/even")
#     strategic_plan = fields.Many2many(comodel_name="strategic.plan.goal", string="SP")
#     # output = fields.Char(string="Output")
#     sp_indicators = fields.Many2one(comodel_name="outcome.indicators", string="Indicator")
#     contribution_to_sdg = fields.Many2many(comodel_name="sdg.configuration", string="Contributing to SDG")
#
#     description_of_the_event = fields.Html(string="Description")
#     achievements = fields.Text(string="Achievements Description")
#     other_resource_utilized = fields.Char(string="Other resource utilised")
#     challenges_encountered = fields.Text(string="Challenges encountered")
#     lesson_learned = fields.Text(string="Lesson learned")
#     way_forward = fields.Text(string="Way forward")
#     unexpected_result = fields.Text(string="Unexpected/Unintended Result")
#
#     # Achievement analysis
#     participant_girl = fields.Boolean('Adolescent girls')
#     participant_boy = fields.Boolean('Adolescent boys')
#     young_women = fields.Boolean('Young women')
#     youth = fields.Boolean('Youth')
#     adult = fields.Boolean('Adult')
#     elders = fields.Boolean('Elders')
#     women = fields.Boolean('women')
#     men = fields.Boolean('Men')
#     mixed = fields.Boolean('Mixed')
#
#     number_of_girls = fields.Integer(string="Number of girls Reached")
#     number_of_boys = fields.Integer(string="Number of boys Reached")
#     number_of_young_women = fields.Integer(string="Number of Young Women Reached")
#     number_of_youth = fields.Integer(string="Number of Youth Reached")
#     number_of_adult = fields.Integer(string="Number of Adult Reached")
#     number_of_elders = fields.Integer(string="Number of Elders Reached")
#     number_of_women = fields.Integer(string="Number of Women Reached")
#     number_of_men = fields.Integer(string="Number of Men Reached")
#     number_of_mixed = fields.Integer(string="Number of Mixed Reached")
#
#     age_group_of_girls = fields.Char(string="Age Group")
#     age_group_of_boys = fields.Char(string="Age Group")
#     age_group_of_young_women = fields.Char(string="Age Group")
#     age_group_of_youth = fields.Char(string="Age Group")
#     age_group_of_adult = fields.Char(string="Age Group")
#     age_group_of_elders = fields.Char(string="Age Group")
#     age_group_of_women = fields.Char(string="Age Group")
#     age_group_of_men = fields.Char(string="Age Group")
#     age_group_of_mixed = fields.Char(string="Age Group")
#
#     # Age group
#     # age_under_18 = fields.Integer(string="Under 18")
#     # between_18_35 = fields.Integer(string="between 18-35")
#     # above_35 = fields.Integer(string="Above 35")
#
#     participant_group_girls = fields.Selection([
#         ('girls', 'Adolescent girls'),
#         ('boys', 'Adolescent boys'),
#         ('young_women', 'Young women'),
#         ('youth', 'Youth'),
#         ('adult', 'Adult'),
#         ('elders', 'Elders'),
#         ('women', 'Women'),
#         ('men', 'Men'),
#         ('mixed', 'Mixed age groups'),
#     ],
#         string="Participant"
#     )
#     # number_of_girls = fields.Integer(string="Number of girls Reached")/
#     #
#     event_location = fields.Selection([
#         ('rural', 'Rural'),
#         ('urban', 'Urban'),
#     ], string="Event Location"
#     )
#
#     activity_addressed = fields.Many2one(comodel_name="project.task", string="Activity addressed")
#     budget_code = fields.Char(string="Budget Code")
#     # currency_id = fields.Many2one("res.currency", string="Currency", required=False,
#     #                               related='activity_addressed.currency_id')
#     budget = fields.Monetary(string="Planed Budget", related='activity_addressed.budget')
#     budget_description_line_ids = fields.One2many(comodel_name="budget.utilized",
#                                                   inverse_name="budget_description_id",
#                                                   string="Budget IDs", required=False, )
#     actual_budget = fields.Monetary(string="Actual Budget", compute='actual_budget_compute')
#     balance = fields.Monetary(string="Balance", compute='balance_compute')
#
#     achievements_reporting_lines = fields.One2many(comodel_name="event.result.achievement",
#                                                    inverse_name="achievements_reporting_id",
#                                                    string="Achievement IDs", required=False, )
#     achievements_output_reporting_lines = fields.One2many(comodel_name="event.result.output.achievement",
#                                                           inverse_name="achievements_output_reporting_id",
#                                                           string="Achievement IDs", required=False, )
#     national_strategic_plan = fields.Many2many("national.strategy.plan", string="National Strategy Plan",
#                                                required=False, )
#     event_attachment_files_lines = fields.One2many(comodel_name="event.attachment.files",
#                                                    inverse_name="event_attachment_id",
#                                                    string="Attachment IDs", required=False, )
#
#     @api.depends('budget', 'actual_budget')
#     def balance_compute(self):
#         for rec in self:
#             rec.balance = rec.budget - rec.actual_budget
#
#     @api.depends('budget_description_line_ids.cost')
#     def actual_budget_compute(self):
#         for rec in self:
#             rec.actual_budget = 0 + sum(line.cost for line in rec.budget_description_line_ids)
#

# class EventAttachmentFiles(models.Model):
#     _name = 'event.attachment.files'
#     _description = 'All result attachment'
#
#     attachment = fields.Binary(string="Attachment", attachment=True, store=True, )
#     attachment_name = fields.Char(string="Attachment Name")
#     attachment_file_name = fields.Char(string="Attachment file")
#     event_attachment_id = fields.Many2one("event.reporting", string="Attachment ID", required=False, )
#
#
# class EventResultAchievement(models.Model):
#     _name = 'event.result.achievement'
#     _description = 'All result achievement are stored in this table'
#
#     @api.onchange('outcome_output_indicator')
#     def _onchange_outcome_output_indicator_id(self):
#         sections = []
#         for section in self.outcome_output_indicator:
#             sections.append(section.id)
#         return {'domain': {'outcome_unit_definition': [('unit_definition_line', 'in', sections)]}}
#
#     @api.onchange('outcome_unit_definition')
#     def _onchange_outcome_unit_definition_id(self):
#         sections = []
#         for section in self.outcome_unit_definition:
#             sections.append(section.id)
#         return {'domain': {'outcome_year': [('unit_line_id', 'in', sections)]}}
#
#     @api.onchange('outcome_year')
#     def _onchange_outcome_year_id(self):
#         sections = []
#         for section in self.outcome_year:
#             sections.append(section.id)
#         return {'domain': {'outcome_actual_period': [('actual_period_section_line', 'in', sections)]}}
#
#     outcome_output_indicator = fields.Many2one(comodel_name='outcome.indicators', string='Outcome Indicator')
#     output_indicator = fields.Many2one(comodel_name='output.indicators', string='Outcome')
#     outcome_unit_definition = fields.Many2one(comodel_name='unit.definition', string='Unit/Definition')
#     outcome_year = fields.Many2one(comodel_name='actual.period.lines', string='Year')
#     actual_value_year = fields.Integer(string='Year Target', related="outcome_year.target_value")
#     outcome_actual_period = fields.Many2one(comodel_name='actual.period.section.lines', string='Period')
#     section_actual_period = fields.Integer(string='Target Value', related='outcome_actual_period.target_actual_value')
#     arrived = fields.Integer(string='Arrived')
#     actual_value = fields.Integer(string='Achievement')
#     achievements_reporting_id = fields.Many2one(comodel_name='event.reporting', string='Achievement ID')
#     gender = fields.Selection([('female', 'Female'), ('men', 'Men'), ], string="Gender")
#
#
# class EventResultOutputAchievement(models.Model):
#     _name = 'event.result.output.achievement'
#     _description = 'All result achievement are stored in this table'
#
#     @api.onchange('outcome_output_indicator')
#     def _onchange_outcome_output_indicator_id(self):
#         sections = []
#         for section in self.outcome_output_indicator:
#             sections.append(section.id)
#         return {'domain': {'outcome_unit_definition': [('output_unit_definition_line', 'in', sections)]}}
#
#     @api.onchange('outcome_unit_definition')
#     def _onchange_outcome_unit_definition_id(self):
#         sections = []
#         for section in self.outcome_unit_definition:
#             sections.append(section.id)
#         return {'domain': {'outcome_year': [('output_unit_line_id', 'in', sections)]}}
#
#     @api.onchange('outcome_year')
#     def _onchange_outcome_year_id(self):
#         sections = []
#         for section in self.outcome_year:
#             sections.append(section.id)
#         return {'domain': {'outcome_actual_period': [('output_actual_period_section_line', 'in', sections)]}}
#
#     outcome_output_indicator = fields.Many2one(comodel_name='output.indicators', string='Output Indicator')
#     outcome_unit_definition = fields.Many2one(comodel_name='output.unit.definition', string='Unit/Definition')
#     outcome_year = fields.Many2one(comodel_name='output.actual.period.lines', string='Year')
#     outcome_actual_period = fields.Many2one(comodel_name='output.actual.period.section.lines', string='Period')
#     actual_value = fields.Integer(string='Value')
#     achievements_output_reporting_id = fields.Many2one(comodel_name='event.reporting', string='Achievement ID')
#
#
# class BudgetUtilized(models.Model):
#     _name = 'budget.utilized'
#     _description = 'Table with the budget utilized'
#     _rec_name = "item"
#
#     item = fields.Char(string="Add Item Description")
#     cost = fields.Float(string="Cost")
#     budget_description_id = fields.Many2one(comodel_name="event.reporting", string="Budget ID",
#                                             required=False, readonly=True)
#
#
# class UnitGoalDefinition(models.Model):
#     _name = 'unit.goal.definition'
#     _description = 'All units goal should be placed here'
#
#     name = fields.Many2one(comodel_name="unit.configuration", string="Unit/Definition", required=False, )
#     unit_location = fields.Many2one(comodel_name="organization.goal.indicators.line", string="Unit/Definition ID",
#                                     required=False, readonly=True)


class UnitConfiguration(models.Model):
    _name = 'unit.configuration'
    _description = 'All units should be placed in unit table'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string="Unit/Definition", required=False, )


class EventsConfigurations(models.Model):
    _name = 'events.configuration'
    _description = 'all events are to create in configurations'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string="Event", required=True, )


class SDGConfigurations(models.Model):
    _name = 'sdg.configuration'
    _description = 'all events are to create in configurations'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string="SDG", required=True, )


class TargetPeriod(models.Model):
    _name = 'target.period'
    _description = 'Target period of the evaluation'
    _rec_name = 'name'

    name = fields.Char(string="Target Period", required=False, )
    period_section_line_ids = fields.One2many(comodel_name="target.period.lines", inverse_name="period_section_id",
                                              string="District IDs", required=False, )


class TargetPeriodLines(models.Model):
    _name = 'target.period.lines'
    _description = 'district line table'

    name = fields.Char(string="Section Period", required=False, )
    period_section_id = fields.Many2one(comodel_name="target.period", string="Section Period", required=False, )


class Region(models.Model):
    _name = 'region'
    _description = 'region table'
    _rec_name = 'name'

    name = fields.Char(string="Region Name", required=False, )
    district_line_ids = fields.One2many(comodel_name="district.lines", inverse_name="district_id",
                                        string="District IDs", required=False, )


class DistrictLine(models.Model):
    _name = 'district.lines'
    _description = 'district line table'

    name = fields.Char(string="District", required=False, )
    district_id = fields.Many2one(comodel_name="region", string="District ID", required=False, )
