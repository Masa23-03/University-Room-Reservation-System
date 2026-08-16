from odoo import models , fields

class LabRequirement(models.Model):
    _name="lab.requirement"
    _description="Lab Requirement Model"

    name=fields.Char(required=True)
    lab_type_ids= fields.Many2many("lab.type" , string="Applicable Lab Type",required=True)
    description=fields.Text()

    _check_name=models.Constraint(
        'UNIQUE(name)',
        "name must be unique"
    )
