from odoo import models, fields


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
