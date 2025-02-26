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
                                                     string="Indicator ID", required=False, )


class KRAOutcomeIndicators(models.Model):
    _name = 'kra.outcome.indicators'
    _rec_name = 'outcome_indicator'

    # outcome_indicator = fields.Many2one(comodel_name="me.indicators", string="Indicator", required=True, )
    outcome_indicator = fields.Char(string="Indicator", required=True, )
    what_to_measure = fields.Char(string="What to measure", required=True)
    baseline_value = fields.Char(string="Baseline Value", required=False)
    kra_outcome_indicator_id = fields.Many2one(comodel_name="key.result.area.outcomes.lines",
                                               string="Outcome Indicator ID",
                                               required=False, readonly=True)
    # unit_definition_line_ids = fields.One2many(comodel_name="unit.definition",
    #                                            inverse_name="unit_definition_line",
    #                                            string="Unit Definition", required=False, )
