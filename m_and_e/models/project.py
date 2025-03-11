from odoo import models, fields, api


class ProgramProject(models.Model):
    _name = 'program.project'
    _description = 'Program Project'

    name = fields.Char(string="Project Name", required=True)
    description = fields.Html(string="Description Project")
    funder = fields.Char(string="Funder")
    currency_id = fields.Many2one('res.currency', string="Currency")
    budget = fields.Monetary(string="Budget", currency_field='currency_id')
    start_date = fields.Date(string="Start Date")
    end_date = fields.Date(string="End Date")
    code = fields.Char(string="Code")
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


class ProgramProjectActualPeriodLines(models.Model):
    _name = 'program.project.actual.period.lines'
    _rec_name = 'actual_period'

    actual_period = fields.Many2one(comodel_name="target.period", string="Actual Period", required=True)
    target_value = fields.Integer(string="Target Value", required=True)
    real_actual_value = fields.Integer(string="Actual value", required=False, default=0, readonly=True)
    target_description = fields.Char(string="Target description", required=False)
    unit_line_id = fields.Many2one(comodel_name="program.project.unit.definition", string="Unit/Definition",
                                   required=False, readonly=True)
    actual_period_section_line_ids = fields.One2many(comodel_name="program.project.actual.period.section.lines",
                                                     inverse_name="actual_period_section_line",
                                                     string="Section Period", required=False, )


class ProgramProjectActualPeriodSectionLines(models.Model):
    _name = 'program.project.actual.period.section.lines'
    _rec_name = 'actual_period_section'

    actual_period_section = fields.Many2one(comodel_name="target.period.lines", string="Actual Section Period",
                                            required=False)
    target_value = fields.Integer(string="Target value", required=False, )
    real_actual_value = fields.Integer(string="Actual value", required=False, readonly=True)
    actual_period_section_line = fields.Many2one(comodel_name="program.project.actual.period.lines",
                                                 string="Actual Period Section",
                                                 required=False, readonly=True)


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
    real_actual_value = fields.Integer(string="Actual value", required=False, default=0, readonly=True)
    target_description = fields.Char(string="Target description", required=False)
    output_unit_line_id = fields.Many2one(comodel_name="program.project.output.unit.definition",
                                          string="Unit/Definition",
                                          required=False, readonly=True)
    output_actual_period_section_line_ids = fields.One2many(
        comodel_name="program.project.output.actual.period.section.lines",
        inverse_name="output_actual_period_section_line",
        string="Section Period", required=False, )


class ProgramProjectOutputActualPeriodSectionLines(models.Model):
    _name = 'program.project.output.actual.period.section.lines'
    _rec_name = 'actual_period_section'

    actual_period_section = fields.Many2one(comodel_name="target.period.lines", string="Actual Section Period",
                                            required=False)
    target_value = fields.Integer(string="Target value", required=False, )
    real_actual_value = fields.Integer(string="Actual value", required=False, readonly=True,
                                       compute="compute_output_total_actual_value")
    output_actual_period_section_line = fields.Many2one(comodel_name="program.project.output.actual.period.lines",
                                                        string="Actual Period Section",
                                                        required=False, readonly=True)

    @api.multi
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

            rec.real_output_actual_value = 0 + current_value


class ProjectActivity(models.Model):
    _name = 'project.activity'

    name = fields.Char(string="Activity", required=True)
    deadline = fields.Date(string="Deadline", required=True)
    currency_id = fields.Many2one('res.currency', string='Currency')
    budget = fields.Monetary(string="Budget", currency_field='currency_id')
    user_id = fields.Many2one(comodel_name="res.users", string="Assigned To", required=True)
    description = fields.Html(string="Description", required=False)
    program_project_activity_id = fields.Many2one(comodel_name="program.project", string="Activity", readonly=True,
                                                  required=False, )
