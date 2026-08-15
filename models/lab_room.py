from odoo import models, fields

class LabRoom(models.Model):
    _name = "lab.room"
    _description = "Lab"

    name = fields.Char(required=True)
    capacity = fields.Integer(required=True)
    floor = fields.Integer(required=True)

    department = fields.Char() # make department into model
    building = fields.Char()   # make building into model
    faculty = fields.Char(required=True)    # make faculty into model

    supervisor_id = fields.Many2one("res.users", required=True)
    lab_type_id = fields.Many2one("lab.type", required=True)

    _check_name = models.Constraint(
        "UNIQUE(name)",
        "Lab name must be unique.",
    )

    _check_capacity=models.Constraint(
        "CHECK(capacity>0)",
        "Lab capacity must be greater than zero.",
    )