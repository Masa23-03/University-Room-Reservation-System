from odoo import models , fields
class LabType(models.Model):
    _name = "lab.type"
    _description = "Lab Type"

    name = fields.Char(required=True)
    description = fields.Text()

    lab_ids = fields.One2many(
        "lab.room",
        "lab_type_id",
    )

    _check_name = models.Constraint(
        "UNIQUE(name)",
        "Lab Type must be unique.",
    )