from odoo import models, fields, api, _

date_format = "%Y-%m-%d"


class StrategicPlanGoal(models.Model):
    _name = 'strategic.plan.goal'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string="Strategic Plan Goal", required=True)
    strategic_plan_indicators_line_ids = fields.One2many(comodel_name="strategic.plan.goal.indicators.line",
                                                         inverse_name="strategic_plan_id",
                                                         string="Strategic plans indicator ID", required=False, )


class StrategicPlanGoalIndicators(models.Model):
    _name = 'strategic.plan.goal.indicators.line'
    _rec_name = 'indicator'

    indicator = fields.Many2one(comodel_name="me.indicators", string="Indicator", required=True, )
    collector = fields.Char(string='Who is collecting')
    actual_value = fields.Char(string='Actual Value')
    strategic_plan_id = fields.Many2one(comodel_name="strategic.plan.goal", string="Outcome Indicator ID",
                                        required=False, readonly=True)
    strategic_plan_indicators_line_ids = fields.One2many(comodel_name="unit.strategy.plan.goal.definition",
                                                         inverse_name="unit_location",
                                                         string="Location", required=False, )


class UnitSPGoalDefinition(models.Model):
    _name = 'unit.strategy.plan.goal.definition'
    _description = 'All units goal should be placed here'

    name = fields.Many2one(comodel_name="unit.configuration", string="Unit/Definition", required=False, )
    unit_location = fields.Many2one(comodel_name="strategic.plan.goal.indicators.line", string="Unit/Definition ID",
                                    required=False, readonly=True)


class SPOutcomes(models.Model):
    _name = 'sp.outcomes'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _rec_name = 'outcome_level'

    outcome_level = fields.Char(string="Outcome level", required=True)
    outcome_goal = fields.Many2one(comodel_name="strategic.plan.goal", string="Goal", required=True)
    description = fields.Text(string="Description", required=True)
    sp_outcome_indicators_line_ids = fields.One2many(comodel_name="sp.outcome.indicators",
                                                     inverse_name="sp_outcome_indicator_id",
                                                     string="Unit IDs", required=False, )


class SPOutcomeIndicators(models.Model):
    _name = 'sp.outcome.indicators'
    _rec_name = 'outcome_indicator'

    outcome_indicator = fields.Many2one(comodel_name="me.indicators", string="Indicator", required=True, )
    what_to_measure = fields.Char(string="What to measure", required=True)
    baseline_value = fields.Char(string="Baseline Value", required=False)
    sp_outcome_indicator_id = fields.Many2one(comodel_name="sp.outcomes", string="Outcome Indicator ID",
                                              required=False, readonly=True)
    unit_definition_line_ids = fields.One2many(comodel_name="sp.unit.definition",
                                               inverse_name="unit_definition_line",
                                               string="Unit Definition", required=False, )


class SPUnitDefinition(models.Model):
    _name = 'sp.unit.definition'
    _rec_name = 'unit'

    unit = fields.Many2one(comodel_name="unit.configuration", string="Unit/Definition", required=False)
    unit_definition_line = fields.Many2one(comodel_name="sp.outcome.indicators", string="Unit/Definition",
                                           required=False,
                                           readonly=True)
    actual_period_line_ids = fields.One2many(comodel_name="sp.actual.period.lines",
                                             inverse_name="unit_line_id",
                                             string="Unit Section", required=False, )


class SPActualPeriodLines(models.Model):
    _name = 'sp.actual.period.lines'
    _rec_name = 'actual_period'

    actual_period = fields.Many2one(comodel_name="target.period", string="Actual Period", required=False)
    target_value = fields.Integer(string="Target Value", required=True)
    target_description = fields.Char(string="Target description", required=True)
    unit_line_id = fields.Many2one(comodel_name="sp.unit.definition", string="Unit/Definition",
                                   required=False, readonly=True)
    actual_period_section_line_ids = fields.One2many(comodel_name="sp.actual.period.section.lines",
                                                     inverse_name="actual_period_section_line",
                                                     string="Section Period", required=False, )


class SPActualPeriodSectionLines(models.Model):
    _name = 'sp.actual.period.section.lines'
    _rec_name = 'actual_period_section'

    actual_period_section = fields.Many2one(comodel_name="target.period.lines", string="Actual Section Period",
                                            required=False)
    target_actual_value = fields.Integer(string="Target value", required=False, )
    real_actual_value = fields.Integer(string="Actual value", required=False, )
    actual_period_section_line = fields.Many2one(comodel_name="sp.actual.period.lines", string="Actual Period Section",
                                                 required=False, readonly=True)


class SPOutputs(models.Model):
    _name = 'sp.output'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _rec_name = 'output_level'

    output_level = fields.Char(string="Output level", required=True)
    outcome_level = fields.Many2one(comodel_name="sp.outcomes", string="Outcome level", required=True)
    description = fields.Text(string="Description", required=True)
    output_indicators_line_ids = fields.One2many(comodel_name="sp.output.indicators",
                                                 inverse_name="output_indicator_id",
                                                 string="Unit IDs", required=False, )


class SPOutputIndicators(models.Model):
    _name = 'sp.output.indicators'
    _rec_name = 'outcome_indicator'

    outcome_indicator = fields.Many2one(comodel_name="me.indicators", string="Indicator", required=True, )
    what_to_measure = fields.Text(string="What to measure", required=True)
    # target = fields.Integer(string="Target", required=True)
    baseline_value = fields.Char(string="Baseline Value", required=False)
    output_indicator_id = fields.Many2one(comodel_name="sp.output", string="Output Indicator ID",
                                          required=False, readonly=True)
    unit_definition_line_ids = fields.One2many(comodel_name="sp.output.unit.definition",
                                               inverse_name="output_unit_definition_line",
                                               string="Unit Definition", required=False, )


class SPOutputUnitDefinition(models.Model):
    _name = 'sp.output.unit.definition'
    _rec_name = 'unit'

    unit = fields.Many2one(comodel_name="unit.configuration", string="Unit/Definition", required=False)
    output_unit_definition_line = fields.Many2one(comodel_name="sp.output.indicators", string="Unit/Definition",
                                                  required=False,
                                                  readonly=True)
    actual_period_line_ids = fields.One2many(comodel_name="sp.output.actual.period.lines",
                                             inverse_name="output_unit_line_id",
                                             string="Unit Section", required=False, )


class SPOutputActualPeriodLines(models.Model):
    _name = 'sp.output.actual.period.lines'
    _rec_name = 'actual_period'

    actual_period = fields.Many2one(comodel_name="target.period", string="Actual Period", required=False)
    target_value = fields.Integer(string="Target Value", required=True)
    target_description = fields.Char(string="Target description", required=True)
    actual_period_line = fields.Many2one(comodel_name="sp.outcome.indicators", string="Actual Period",
                                         required=False, readonly=True)
    output_unit_line_id = fields.Many2one(comodel_name="sp.output.unit.definition", string="Unit/Definition",
                                          required=False, readonly=True)
    actual_period_section_line_ids = fields.One2many(comodel_name="sp.output.actual.period.section.lines",
                                                     inverse_name="output_actual_period_section_line",
                                                     string="Section Period", required=False, )


class OutputActualPeriodSectionLines(models.Model):
    _name = 'sp.output.actual.period.section.lines'
    _rec_name = 'actual_period_section'

    actual_period_section = fields.Many2one(comodel_name="target.period.lines", string="Actual Section Period",
                                            required=False)
    real_output_actual_value = fields.Integer(string="Output Actual value", required=False, )
    output_actual_period_section_line = fields.Many2one(comodel_name="sp.actual.period.lines",
                                                        string="Actual Period Section",
                                                        required=False, readonly=True)


class StrategicPlan(models.Model):
    _name = 'strategic.plan'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string="Strategic Plan", required=True)
    strategic_plan_indicators_line_ids = fields.One2many(comodel_name="strategic.plan.indicators.line",
                                                         inverse_name="strategic_plan_id",
                                                         string="Strategic plans indicator ID", required=False, )


class StrategicPlanIndicators(models.Model):
    _name = 'strategic.plan.indicators.line'
    _rec_name = 'indicator'

    indicator = fields.Many2one(comodel_name="me.indicators", string="Indicator", required=True, )
    strategic_plan_id = fields.Many2one(comodel_name="strategic.plan", string="Outcome Indicator ID",
                                        required=False, readonly=True)
