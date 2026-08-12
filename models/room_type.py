from odoo import models , fields
class RoomType(models.Model):
    _name= "room.type"
    _description= "Room Type Model"

    name= fields.Char(required=True)
    description = fields.Text()
    # room_ids= fields.One2many('')

    _check_name=models.Constraint(
        'UNIQUE(name)',
        'Room Type must be Unique'
    )