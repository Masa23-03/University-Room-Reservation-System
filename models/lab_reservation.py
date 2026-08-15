from odoo import models, fields
from dateutil.relativedelta import relativedelta

class LabReservation (models.Model):
    _name="lab.reservation"
    _description="Lab Reservation Model"

    
    requester_id=fields.Many2one("res.users" , required=True , default=lambda self: self.env.user)
    purpose= fields.Char(default="Exam")
    course_name= fields.Char(string="Course")
    start_datetime= fields.Datetime(string="Start Date" , default=fields.Datetime.now() + relativedelta(weeks=1))
    end_datetime= fields.Datetime(string="End Date" , default = fields.Datetime.now()+relativedelta(weeks=1))
    number_of_participants= fields.Integer(string="Number of Students",default=20)
    lab_ids= fields.Many2many("lab.room")
    internet_required=fields.Boolean(string="Internet Required" , default= False)
    requirement_ids= fields.Many2many("lab.requirement"  , string="Requirements")

    status= fields.Selection(
        selection=[
            ('draft' , 'Draft')
            ('pending' , 'Pending'),
            ('confirmed' , 'Confirmed'),
            ('cancelled' , 'Cancelled'),
            ('rejected' , 'Rejected'),
            ('completed' , 'Completed')

        ],default='draft' , required=True
    )

    rejection_reason=fields.Text()

    _check_dates= models.Constraint(
        'CHECK(start_datetime < end_datetime)',
        "Start date time should be before end date time"
    )
    _check_number_of_participants=models.Constraint(
        'CHECK(number_of_participants >0)',
        'Number of students must be positive'
    )


