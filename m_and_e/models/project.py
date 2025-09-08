from odoo import models, fields, api


class ProgramProject(models.Model):
    _name = 'program.project'
    _description = 'Program Project'

    name = fields.Char(string="Project Name", required=True)
    description = fields.Html(string="Description Project")
    funder = fields.Char(string="Funder")
    sp_id = fields.Many2one(comodel_name="key.result.area", string="SP", required=False)
    currency_id = fields.Many2one('res.currency', string="Currency")
    budget = fields.Monetary(string="Budget", currency_field='currency_id')
    start_date = fields.Date(string="Start Date")
    end_date = fields.Date(string="End Date")
    code = fields.Char(string="Code")

    target_outcome_result = fields.Integer(string="Target Outcome Indicator Result", compute="_compute_outcome_results",
                                           store=True)
    actual_outcome_result = fields.Integer(string="Actual Outcome Indicator Result", compute="_compute_outcome_results",
                                           store=True)
    outcome_success_percent = fields.Float(string="Outcome Success (%)", compute="_compute_outcome_results", store=True)

    target_output_result = fields.Integer(string="Target Output Indicator Result", compute="_compute_output_results",
                                          store=True)
    actual_output_result = fields.Integer(string="Actual Output Indicator Result", compute="_compute_output_results",
                                          store=True)
    output_success_percent = fields.Float(string="Output Success (%)", compute="_compute_output_results", store=True)

    total_budget_used = fields.Monetary(string="Total Budget Used", currency_field='currency_id')
    total_budget_remain = fields.Monetary(string="Total Budget Remain", currency_field='currency_id')
    active = fields.Boolean(string="Active", default=True)
    program_project_outcome_line_ids = fields.One2many(comodel_name="program.project.outcomes.lines",
                                                       inverse_name="program_project_id",
                                                       string="Outcome", required=False)
    program_output_line_ids = fields.One2many(comodel_name="program.project.output.lines",
                                              inverse_name="program_project_output_id",
                                              string="Output", required=False)

    project_activities_line_ids = fields.One2many(comodel_name="project.activity",
                                                  inverse_name="program_project_activity_id",
                                                  string="Activity", required=False)

    # @api.depends('program_project_outcome_line_ids.program_outcome_indicator_line_ids.unit_definition_line_ids'
    #              '.actual_period_line_ids.target_value')
    # def _compute_outcome_target(self):
    #     for rec in self:
    #         total_target_value = 0
    #         for outcome in rec.program_project_outcome_line_ids:
    #             for indicator in outcome.program_outcome_indicator_line_ids:
    #                 for unit in indicator.unit_definition_line_ids:
    #                     for period in unit.actual_period_line_ids:
    #                         total_target_value += period.target_value
    #
    #         rec.target_outcome_result = total_target_value


    @api.depends('program_project_outcome_line_ids.program_outcome_indicator_line_ids.unit_definition_line_ids'
                 '.actual_period_line_ids.target_value',
                 'program_project_outcome_line_ids.program_outcome_indicator_line_ids.unit_definition_line_ids'
                 '.actual_period_line_ids.real_actual_value_year')
    def _compute_outcome_results(self):
        for project in self:
            target_total = 0
            actual_total = 0

            for outcome in project.program_project_outcome_line_ids:
                for indicator in outcome.program_outcome_indicator_line_ids:
                    for unit in indicator.unit_definition_line_ids:
                        for period in unit.actual_period_line_ids:
                            target_total += period.target_value
                            actual_total += period.real_actual_value_year

            project.target_outcome_result = target_total
            project.actual_outcome_result = actual_total
            project.outcome_success_percent = (actual_total / target_total * 100) if target_total > 0 else 0

    def _compute_output_results(self):
        for project in self:
            target_total = 0
            actual_total = 0

            for output in project.program_output_line_ids:
                for indicator in output.program_output_indicator_line_ids:
                    for unit in indicator.program_output_unit_definition_line_ids:
                        for period in unit.output_actual_period_line_ids:
                            target_total += period.target_value
                            actual_total += period.real_actual_value

            project.target_output_result = target_total
            project.actual_output_result = actual_total
            project.output_success_percent = (actual_total / target_total * 100) if target_total > 0 else 0


class ProgramProjectOutcome(models.Model):
    _name = 'program.project.outcomes.lines'
    _rec_name = 'outcome_level'

    outcome_level = fields.Char(string="Outcome level", required=True)
    description = fields.Text(string="Description", required=True)

    program_project_id = fields.Many2one(comodel_name="program.project", string="Project program", readonly=True,
                                         required=False, )
    program_outcome_indicator_line_ids = fields.One2many(comodel_name="program.project.outcome.indicators",
                                                         inverse_name="program_outcome_indicator_id",
                                                         string="Indicator", required=False, )


class ProgramProjectIndicators(models.Model):
    _name = 'program.project.outcome.indicators'
    _rec_name = 'outcome_indicator'

    outcome_indicator = fields.Many2one(comodel_name="me.indicators", string="Indicator", required=True, )
    what_to_measure = fields.Char(string="What to measure", required=True)
    baseline_value = fields.Char(string="Baseline Value", required=False)
    program_outcome_indicator_id = fields.Many2one(comodel_name="program.project.outcomes.lines",
                                                   string="Outcome Indicator",
                                                   required=False, readonly=True)
    unit_definition_line_ids = fields.One2many(comodel_name="program.project.unit.definition",
                                               inverse_name="unit_definition_line",
                                               string="Unit Definition", required=False, )


class ProgramProjectUnitDefinition(models.Model):
    _name = 'program.project.unit.definition'
    _rec_name = 'unit'

    unit = fields.Many2one(comodel_name="unit.configuration", string="Unit/Definition", required=True)
    unit_definition_line = fields.Many2one(comodel_name="program.project.outcome.indicators", string="Unit/Definition",
                                           required=False,
                                           readonly=True)
    actual_period_line_ids = fields.One2many(comodel_name="program.project.actual.period.lines",
                                             inverse_name="unit_line_id",
                                             string="Unit Section", required=False, )


# class ProgramProjectActualPeriodLines(models.Model):
#     _name = 'program.project.actual.period.lines'
#     _rec_name = 'actual_period'
#
#     actual_period = fields.Many2one(comodel_name="target.period", string="Actual Period", required=True)
#     target_value = fields.Integer(string="Target Value", required=True, store=True)
#     real_actual_value = fields.Integer(string="Actual value", required=False, default=0, readonly=True,
#                                        compute="_compute_total_actual_value", store=True)
#     target_description = fields.Char(string="Target description", required=False)
#     unit_line_id = fields.Many2one(comodel_name="program.project.unit.definition", string="Unit/Definition",
#                                    required=False, readonly=True)
#     actual_period_section_line_ids = fields.One2many(comodel_name="program.project.actual.period.section.lines",
#                                                      inverse_name="actual_period_section_line",
#                                                      string="Section Period", required=False, )
#
#
#     # def _compute_total_actual_value(self):
#     #     # self : model shift
#     #     achievement = self.env['event.result.achievement']
#     #     for rec in self:
#     #         current_value = 0
#     #         achievement_ids = achievement.search([('outcome_year', '=', rec.actual_period.id)])
#     #         if achievement_ids:
#     #             for achievement in achievement_ids:
#     #                 # amount = achievement amount
#     #                 current_value += achievement.actual_value
#     #
#     #         rec.real_actual_value = 0 + current_value
#
#     # @api.depends('actual_period_section_line_ids.real_actual_value')
#     # def _compute_total_actual_value(self):
#     #     # for value in self:
#     #     total = 0.0
#     #     for actual_value in self:
#     #         total += sum(line.real_actual_value for line in actual_value.actual_period_section_line_ids)
#     #
#     #         actual_value.real_actual_value = total
#
#     @api.depends('actual_period_section_line_ids.real_actual_value')
#     def _compute_total_actual_value(self):
#         for record in self:
#             record.real_actual_value = sum(
#                 line.real_actual_value for line in record.actual_period_section_line_ids
#             )



class ProgramProjectActualPeriodLines(models.Model):
    _name = 'program.project.actual.period.lines'
    _rec_name = 'actual_period'

    actual_period = fields.Many2one(comodel_name="target.period", string="Actual Period", required=True)
    target_value = fields.Integer(string="Target Value", required=True, store=True)
    real_actual_value_year = fields.Integer(
        string="Actual value",
        compute="_compute_total_actual_value",
        readonly=True,
        default=0
    )
    target_description = fields.Char(string="Target description", required=False)
    unit_line_id = fields.Many2one(comodel_name="program.project.unit.definition", string="Unit/Definition")
    actual_period_section_line_ids = fields.One2many(
        comodel_name="program.project.actual.period.section.lines",
        inverse_name="actual_period_section_line",
        string="Section Period"
    )

    # @api.depends('actual_period_section_line_ids.real_actual_value')
    # def _compute_total_actual_value(self):
    #     for record in self:
    #         record.real_actual_value_year = sum(
    #             line.real_actual_value for line in record.actual_period_section_line_ids
    #         )


    def _compute_total_actual_value(self):
        # self : model shift
        achievement = self.env['event.result.achievement']
        for rec in self:
            current_value = 0
            achievement_ids = achievement.search([('outcome_year', '=', rec.id)])
            if achievement_ids:
                for achievement in achievement_ids:
                    # amount = achievement amount
                    current_value += achievement.actual_value

            rec.real_actual_value_year = 0 + current_value
    #         # rec.real_actual_value = 90

    #
    # def _compute_outcome_total_actual_value(self):
    #     # self : model shift
    #     achievement = self.env['event.result.achievement']
    #     for rec in self:
    #         current_value = 0
    #         achievement_ids = achievement.search([('outcome_actual_period', '=', rec.id)])
    #         if achievement_ids:
    #             for achievement in achievement_ids:
    #                 # amount = achievement amount
    #                 current_value += achievement.actual_value
    #
    #         rec.real_actual_value = 0 + current_value





    # @api.depends('actual_period_section_line_ids.real_actual_value')
    # def _compute_total_actual_value(self):
    #     for record in self:
    #         record.real_actual_value = sum(
    #             line.real_actual_value for line in record.actual_period_section_line_ids
    #         )



class ProgramProjectActualPeriodSectionLines(models.Model):
    _name = 'program.project.actual.period.section.lines'
    _rec_name = 'actual_period_section'

    actual_period_section = fields.Many2one(comodel_name="target.period.lines", string="Actual Section Period",
                                            required=False)
    target_value = fields.Integer(string="Target value", required=False, store=True)
    real_actual_value = fields.Integer(string="Actual value", required=False, readonly=True,
                                       compute="_compute_outcome_total_actual_value")
    actual_period_section_line = fields.Many2one(comodel_name="program.project.actual.period.lines",
                                                 string="Actual Period",
                                                 required=False, readonly=True)

    outcome_indicator = fields.Many2one(
        related="actual_period_section_line.unit_line_id.unit_definition_line.outcome_indicator",
        string="Outcome Indicator", store=True, readonly=True
    )

    # Related Project ID for Grouping
    project_id = fields.Many2one(
        comodel_name="program.project",
        string="Project",
        store=True,
        readonly=True,
        related="actual_period_section_line.unit_line_id.unit_definition_line.program_outcome_indicator_id.program_project_id"
    )

    # Success Percentage Field
    success_percentage = fields.Float(
        string="Success Percentage",
        compute="_compute_success_percentage",

    )

    @api.depends('real_actual_value', 'target_value')
    def _compute_success_percentage(self):
        for rec in self:
            if rec.target_value and rec.target_value > 0:
                rec.success_percentage = (rec.real_actual_value / rec.target_value) * 100
            else:
                rec.success_percentage = 0.0


    def _compute_outcome_total_actual_value(self):
        # self : model shift
        achievement = self.env['event.result.achievement']
        for rec in self:
            current_value = 0
            achievement_ids = achievement.search([('outcome_actual_period', '=', rec.id)])
            if achievement_ids:
                for achievement in achievement_ids:
                    # amount = achievement amount
                    current_value += achievement.actual_value

            rec.real_actual_value = 0 + current_value




class ProgramProjectOutput(models.Model):
    _name = 'program.project.output.lines'
    _rec_name = 'output_level'

    output_level = fields.Char(string="Output level", required=True)
    description = fields.Text(string="Description", required=True)
    program_project_output_id = fields.Many2one(comodel_name="program.project", string="Output", readonly=True,
                                                required=False, )
    program_output_indicator_line_ids = fields.One2many(comodel_name="program.project.output.indicators",
                                                        inverse_name="program_output_indicator_id",
                                                        string="Indicator", required=False, )


class ProgramProjectOutputIndicators(models.Model):
    _name = 'program.project.output.indicators'
    _rec_name = 'output_indicator'

    output_indicator = fields.Many2one(comodel_name="me.indicators", string="Indicator", required=True, )
    what_to_measure = fields.Char(string="What to measure", required=True)
    baseline_value = fields.Char(string="Baseline Value", required=False)
    program_output_indicator_id = fields.Many2one(comodel_name="program.project.output.lines",
                                                  string="Output Indicator",
                                                  required=False, readonly=True)
    program_output_unit_definition_line_ids = fields.One2many(comodel_name="program.project.output.unit.definition",
                                                              inverse_name="output_unit_definition_line",
                                                              string="Unit Definition", required=False, )


class ProgramProjectOutputUnitDefinition(models.Model):
    _name = 'program.project.output.unit.definition'
    _rec_name = 'unit'

    unit = fields.Many2one(comodel_name="unit.configuration", string="Unit/Definition", required=True)
    output_unit_definition_line = fields.Many2one(comodel_name="program.project.output.indicators",
                                                  string="Unit/Definition",
                                                  required=False,
                                                  readonly=True)
    output_actual_period_line_ids = fields.One2many(comodel_name="program.project.output.actual.period.lines",
                                                    inverse_name="output_unit_line_id",
                                                    string="Unit Section", required=False, )


class ProgramProjectOutputActualPeriodLines(models.Model):
    _name = 'program.project.output.actual.period.lines'
    _rec_name = 'actual_period'

    actual_period = fields.Many2one(comodel_name="target.period", string="Actual Period", required=True)
    target_value = fields.Integer(string="Target Value", required=True)
    real_actual_value = fields.Integer(string="Actual value", required=False, default=0, readonly=True,
                                       compute="compute_total_actual_value")
    target_description = fields.Char(string="Target description", required=False)
    output_unit_line_id = fields.Many2one(comodel_name="program.project.output.unit.definition",
                                          string="Unit/Definition",
                                          required=False, readonly=True)
    output_actual_period_section_line_ids = fields.One2many(
        comodel_name="program.project.output.actual.period.section.lines",
        inverse_name="output_actual_period_section_line",
        string="Section Period", required=False, )

    output_indicator = fields.Many2one(related="output_unit_line_id.output_unit_definition_line.output_indicator",
                                       string="Output Indicator", store=True, readonly=True)

    percentage_result = fields.Float(string="Percentage Result", compute="_compute_percentage_result", store=True)

    @api.depends('target_value', 'real_actual_value')
    def _compute_percentage_result(self):
        for record in self:
            if record.target_value > 0:
                record.percentage_result = (record.real_actual_value / record.target_value) * 100
            else:
                record.percentage_result = 0


    # def compute_total_actual_value(self):
    #     # self : model shift
    #     achievement = self.env['event.result.output.achievement']
    #     for rec in self:
    #         current_value = 0
    #         achievement_ids = achievement.search([('outcome_year.id', '=', rec.actual_period.id)])
    #         if achievement_ids:
    #             for achievement in achievement_ids:
    #                 # amount = achievement amount
    #                 current_value += achievement.actual_value
    #
    #         rec.real_actual_value = 0 + current_value
    #

    @api.depends('output_actual_period_section_line_ids.real_actual_value')
    def compute_total_actual_value(self):
        # for value in self:
        total = 0.0
        for actual_value in self:
            total += sum(line.real_actual_value for line in actual_value.output_actual_period_section_line_ids)

            actual_value.real_actual_value = total



class ProgramProjectOutputActualPeriodSectionLines(models.Model):
    _name = 'program.project.output.actual.period.section.lines'
    _rec_name = 'actual_period_section'

    actual_period_section = fields.Many2one(comodel_name="target.period.lines", string="Actual Section Period",
                                            required=False)
    target_value = fields.Integer(string="Target value", required=False, )
    real_actual_value = fields.Integer(string="Actual value", required=False, readonly=True,
                                       compute="compute_output_total_actual_value")
    output_actual_period_section_line = fields.Many2one(comodel_name="program.project.output.actual.period.lines",
                                                        string="Actual Period",
                                                        required=False, readonly=True)

    percentage_result = fields.Float(string="Success %", compute="_compute_success_percentage")
    output_indicator = fields.Many2one(
        related="output_actual_period_section_line.output_unit_line_id.output_unit_definition_line.output_indicator",
        string="Output Indicator", store=True, readonly=True
    )

    project_id = fields.Many2one(
        comodel_name="program.project", string="Project", store=True, readonly=True,
        related="output_actual_period_section_line.output_unit_line_id.output_unit_definition_line.program_output_indicator_id.program_project_output_id"

    )

    @api.depends('target_value', 'real_actual_value')
    def _compute_success_percentage(self):
        for rec in self:
            if rec.target_value > 0:
                rec.percentage_result = (rec.real_actual_value / rec.target_value) * 100
            else:
                rec.percentage_result = 0


    def compute_output_total_actual_value(self):
        # self : model shift
        achievement = self.env['event.result.output.achievement']
        for rec in self:
            current_value = 0
            achievement_ids = achievement.search([('outcome_actual_period', '=', rec.id)])
            if achievement_ids:
                for achievement in achievement_ids:
                    # amount = achievement amount
                    current_value += achievement.actual_value

            rec.real_actual_value = 0 + current_value


class ProjectActivity(models.Model):
    _name = 'project.activity'

    state = fields.Selection([
        ('not_started', 'Not started'),
        ('in_progress', 'In Progress'),
        ('completed', 'Completed'),
        ('cancel', 'Cancel'),

    ],
        string="Status", default='not_started',
        track_visibility='onchange', )


    def button_started(self):
        self.write({'state': 'in_progress'})
        return True


    def button_completed(self):
        self.write({'state': 'completed'})
        return True

    name = fields.Char(string="Activity", required=True)
    deadline = fields.Date(string="Deadline", required=True)
    currency_id = fields.Many2one('res.currency', string='Currency')
    budget = fields.Monetary(string="Budget", currency_field='currency_id')
    user_id = fields.Many2one(comodel_name="res.users", string="Assigned To", required=True)
    description = fields.Html(string="Description", required=False)
    program_project_activity_id = fields.Many2one(comodel_name="program.project", string="Activity", readonly=True,
                                                  required=False, )
    project_name = fields.Char(string="Project Name", related="program_project_activity_id.name", store=True)

