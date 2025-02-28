from odoo import models, fields, api, _

date_format = "%Y-%m-%d"


class KeyResultArea(models.Model):
    _name = 'key.result.area'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string="Name", required=True)
    outcome_line_ids = fields.One2many(comodel_name="key.result.area.outcomes.lines",
                                       inverse_name="key_result_area_id",
                                       string="Outcome ID", required=False)


class KeyResultAreaOutcome(models.Model):
    _name = 'key.result.area.outcomes.lines'
    _rec_name = 'outcome_level'

    outcome_level = fields.Char(string="Outcome level", required=True)
    description = fields.Text(string="Description", required=True)
    key_result_area_id = fields.Many2one(comodel_name="key.result.area", string="KRA ID", readonly=True,
                                         required=False, )
    kra_outcome_indicator_line_ids = fields.One2many(comodel_name="kra.outcome.indicators",
                                                     inverse_name="kra_outcome_indicator_id",
                                                     string="Indicator", required=False, )


class KRAOutcomeIndicators(models.Model):
    _name = 'kra.outcome.indicators'
    _rec_name = 'outcome_indicator'

    outcome_indicator = fields.Many2one(comodel_name="me.indicators", string="Indicator", required=True, )
    what_to_measure = fields.Char(string="What to measure", required=True)
    baseline_value = fields.Char(string="Baseline Value", required=False)
    kra_outcome_indicator_id = fields.Many2one(comodel_name="key.result.area.outcomes.lines",
                                               string="Outcome Indicator",
                                               required=False, readonly=True)
    unit_definition_line_ids = fields.One2many(comodel_name="sp.unit.definition",
                                               inverse_name="unit_definition_line",
                                               string="Unit Definition", required=False, )


class SPUnitDefinition(models.Model):
    _name = 'sp.unit.definition'
    _rec_name = 'unit'

    unit = fields.Many2one(comodel_name="unit.configuration", string="Unit/Definition", required=True)
    unit_definition_line = fields.Many2one(comodel_name="kra.outcome.indicators", string="Unit/Definition",
                                           required=False,
                                           readonly=True)
    actual_period_line_ids = fields.One2many(comodel_name="sp.actual.period.lines",
                                             inverse_name="unit_line_id",
                                             string="Unit Section", required=False, )


class SPActualPeriodLines(models.Model):
    _name = 'sp.actual.period.lines'
    _rec_name = 'actual_period'

    actual_period = fields.Many2one(comodel_name="target.period", string="Actual Period", required=True)
    target_value = fields.Integer(string="Target Value", required=True)
    real_actual_value = fields.Integer(string="Actual value", required=False, default=0, readonly=True)
    target_description = fields.Char(string="Target description", required=False)
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
    target_value = fields.Integer(string="Target value", required=False, )
    real_actual_value = fields.Integer(string="Actual value", required=False, readonly=True)
    actual_period_section_line = fields.Many2one(comodel_name="sp.actual.period.lines", string="Actual Period Section",
                                                 required=False, readonly=True)
