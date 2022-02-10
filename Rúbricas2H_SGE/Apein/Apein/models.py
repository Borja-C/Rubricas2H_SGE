from datetime import date
from dateutil.relativedelta import *
from odoo.exceptions import ValidationError
from odoo import models, fields, api


class person(models.Model):
    _name = "person"
    dni = fields.Char(string="dni", required=True)


class provider(models.Model):
    _inherit = "person"
    _name = "provider"
    provider_name = fields.Char(string="name")
    order_number = fields.One2many(
        "providerorder", "order_number", string="order number")
    components = fields.Many2many("component", "component_provider",
                                  "component_code", "dni", "provider")


class component(models.Model):
    _name = "component"
    component_code = fields.Integer(
        string="component's id", required=True, unique=True)
    description = fields.Char(string="component's description")
    trademark_code = fields.One2many(
        "trademark", "trademark_code", string="trademark code")
    providers = fields.Many2many("provider", "component_provider",
                                 "dni", "component_code", "component")
    _sql_constraints = [('component_code', 'UNIQUE (component_code)',
                         'component id already in use')]


class trademark(models.Model):
    _name = "trademark"
    trademark_code = fields.Integer(
        string="trademark's id", required=True, unique=True)
    trademark_name = fields.Char(string="trademark's name")
    component_code = fields.Many2one("component", string="component code")


class providerorder(models.Model):
    _name = "providerorder"
    order_number = fields.Integer(
        string="order's number", required=True, unique=True)
    order_date = fields.Date(string="order's date", store=True)
    order_days = fields.Integer(
        compute='_compute_field_name', string="order's duration days", store=True)
    provider_dni = fields.Many2one("provider", string="provider's dni")
    provider_orderline = fields.One2many(
        "providerorderline", "line_code", string="provider's line code")

    @api.constrains('order_days')
    def _check_days(self):
        for record in self:
            if record.order_days < 1:
                raise ValidationError("you can't order in one day")

    @api.constrains('order_date')
    def _constrains_order_date(self):
        for r in self:
            hoy = date.today()
            if r.order_date < hoy:
                raise ValidationError("asdasd")

    @api.depends('order_days')
    def _compute_order_days(self):
        for r in self:
            today = date.today()
            r.order_days = relativedelta(today, r.order_date).days


class providerorderline(models.Model):
    _name = "providerorderline"
    line_code = fields.Integer(
        string="provider order line id", required=True, unique=True)
    unit_number = fields.Integer(string="number of units")
    ordernumber = fields.Many2one("providerorder", string="order number")
