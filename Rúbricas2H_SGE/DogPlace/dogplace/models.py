
from odoo import models, fields, api


class person(models.Model):
    _name="person"
    name = fields.Char(string="name", required=True)
    dni = fields.Char(string="dni")
    surname = fields.Char(string="surname")
    dogs_id = fields.One2many("dogs", "person_id", string="owned dogs")
    adoption_id = fields.One2many("adoption", "person_id", string="adoptions")



class animal(models.Model):
    _name = "animal"
    breed = breed = fields.Char(string="animal's breed")
    heigth = fields.Integer(string="animal's heigth(cm)")
    


class dogs(models.Model):
    _name = "dogs"
    _inherit = "animal"
    name = fields.Char(string="name", required=True)
    person_id = fields.Many2one("person", string="associated person")
    adoption_id = fields.One2many("adoption","dogs_id", string="adopted by")



class adoption(models.Model):
    _name = "adoption"
    adoption_date = fields.Date(string="Adoption's Day",
                             store=True,
                             default=fields.Date.today)
    person_id = fields.Many2one("person", string="owner")
    dogs_id = fields.Many2one("dogs", string="dog")

