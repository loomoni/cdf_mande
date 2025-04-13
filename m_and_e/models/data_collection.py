from odoo import models, fields, api, _


class ProjectBeneficiary(models.Model):
    _name = 'project.beneficiary'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Project Beneficiary'

    project_name = fields.Many2one(comodel_name="program.project", string='Project Name')
    goal = fields.Text(string='Goal')
    region = fields.Many2one(comodel_name="region", string='Region')
    district = fields.Many2one(comodel_name="district.lines", string='District')
    ward = fields.Char(string='Ward')
    village = fields.Char(string='Village')
    date = fields.Date(string='Date')
    name = fields.Char(string='Name of Beneficiary')
    contact = fields.Char(string='Contact')
    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female'),
    ], string='Gender')
    age = fields.Integer(string='Age')
    education_level = fields.Char(string='Education Level')
    disability = fields.Selection([
        ('yes', 'Yes'),
        ('no', 'No'),
    ], string='Disability')
    vulnerability_status = fields.Selection([
        ('Health', 'Health'),
        ('Protection', 'Protection'),
        ('Economic', 'Economic'),
    ], string='Vulnerability Status')

    #  Health information is up

    tested_hiv_positive = fields.Selection([
        ('yes', 'Yes'),
        ('no', 'No'),
    ], string='Tested HIV Positive')

    new_hiv_tested_cases = fields.Selection([
        ('yes', 'Yes'),
        ('no', 'No'),
    ], string='New HIV Tested Cases')

    started_arv = fields.Selection([
        ('yes', 'Yes'),
        ('no', 'No'),
    ], string='Started ARV (If New Client)')

    reasons_not_taking_arv = fields.Text(string='Reasons for Not Taking ARV')

    prevention_methods = fields.Selection([
        ('condom_use', 'Condom use'),
        ('prep', 'PrEP'),
        ('vmmc', 'VMMC'),
        ('abstinence', 'Abstinence'),
        ('others', 'Others'),
    ], string='Prevention Methods')

    adherence_level = fields.Selection([
        ('Low', 'Low'),
        ('Medium', 'Medium'),
        ('High', 'High')
    ], string='Adherence Level')

    # Violence and recovery section
    type_of_violence = fields.Selection([
        ('physical', 'Physical'),
        ('emotional', 'Emotional'),
        ('sexual', 'Sexual'),
        ('neglect', 'Neglect'),
        ('other', 'Other'),
    ], string='Type of Violence')

    violence_reported_by = fields.Selection([
        ('self', 'Self'),
        ('teacher', 'Teacher'),
        ('student', 'Student'),
        ('parent', 'Parent'),
        ('relative', 'Relative'),
        ('other', 'Other'),
    ], string='Who Reported the Violence Case')

    support_services_accessed = fields.Selection([
        ('counseling', 'Counseling'),
        ('legal_aid', 'Legal Aid'),
        ('medical_care', 'Medical Care'),
        ('shelter', 'Shelter'),
        ('gender_desk', 'Gender Desk / Police Services'),
        ('other', 'Other'),
    ], string='Support Services Accessed')

    psychotherapy_received = fields.Selection([
        ('yes', 'Yes'),
        ('no', 'No'),
    ], string='Survivors Received Psychotherapy')

    level_of_recovery = fields.Selection([
        ('full', 'Full'),
        ('partial', 'Partial'),
        ('ongoing', 'Ongoing Challenges'),
    ], string='Level of Recovery')

    barriers_to_recovery = fields.Text(string='Barriers to Recovery')

    perception_of_safety = fields.Text(string='Perception of Safety')

    case_status = fields.Selection([
        ('within_6_months', 'Decided within six months'),
        ('above_6_months', 'Decided above six months'),
    ], string='Status of the Case')

# Economic Vulnerability

    type_of_iga = fields.Selection([
        ('agriculture', 'Agriculture'),
        ('trade', 'Trade'),
        ('crafts', 'Crafts'),
    ], string='Type of IGA involved')

    start_date = fields.Date(string='Start date of IGA')

    member_vsla = fields.Selection([
        ('yes', 'Yes'),
        ('no', 'No'),
    ], string='Member of VSLA')

    vsla_functional = fields.Selection([
        ('yes', 'Yes'),
        ('no', 'No'),
    ], string='If Yes, is VSLA functional')

    monthly_revenue = fields.Monetary(string='Monthly revenue', currency_field='currency_id')
    amount_saved_per_month = fields.Monetary(string='Amount saved per month', currency_field='currency_id')
    monthly_income_category = fields.Selection([
        ('below_poverty_line', 'Below poverty line'),
        ('at_poverty_line', 'At poverty line'),
        ('above_poverty_line', 'Above poverty line'),
    ], string='Monthly income categorized as')

    saving_scheme = fields.Selection([
        ('vicoba', 'VICOBA'),
        ('microfinance', 'Microfinance'),
        ('bank', 'Bank'),
        ('other', 'Other'),
    ], string='Saving scheme')

    training_attended = fields.Selection([
        ('financial_lite', 'financial literacy'),
        ('business_management', 'business management'),
        ('skill_development', 'skills development (multiple)'),
        ('other', 'Other'),
    ], string='Training attended')

    training_facilitated_by = fields.Selection([
        ('CDF,', 'CDF'),
        ('SIDO', 'SIDO'),
        ('Governmentcouncil', 'Government council'),
        ('other', 'Other'),
    ],  string='Training Facilitated by')

    currency_id = fields.Many2one('res.currency', string='Currency')