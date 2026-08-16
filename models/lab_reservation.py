from odoo import models, fields ,api
from dateutil.relativedelta import relativedelta

class LabReservation (models.Model):
    _name="lab.reservation"
    _description="Lab Reservation Model"

    name= fields.Char(string="Reservation Reference", default='New' , readonly=True , copy=False)
    requester_id=fields.Many2one("res.users" , required=True , default=lambda self: self.env.user)
    purpose= fields.Char( default="Exam",required=True)
    course_name= fields.Char(string="Course")
    start_datetime= fields.Datetime(string="Start Date" ,required=True, default=lambda self: fields.Datetime.now() + relativedelta(weeks=1))
    end_datetime= fields.Datetime(string="End Date" , required=True,default =lambda self: fields.Datetime.now()+relativedelta(weeks=1 , hours=2))
    number_of_participants= fields.Integer(string="Number of Students", required=True,default=20)
    lab_ids= fields.Many2many("lab.room", string="Labs", required=True)
    requirement_ids= fields.Many2many("lab.requirement"  , string="Requirements")

    state= fields.Selection(
        selection=[
            ('draft' , 'Draft'),
            ('pending' , 'Pending'),
            ('confirmed' , 'Confirmed'),
            ('cancelled' , 'Cancelled'),
            ('rejected' , 'Rejected'),
            ('completed' , 'Completed')

        ],default='draft' , required=True
    )

    notes=fields.Text(string="Additional Notes")

    rejection_reason=fields.Text()
    

    _check_dates= models.Constraint(
        'CHECK(start_datetime < end_datetime)',
        "Start date time should be before end date time"
    )
    _check_number_of_participants=models.Constraint(
        'CHECK(number_of_participants >0)',
        'Number of students must be positive'
    )

    @api.model_create_multi
    def create(self,vals_list):
        for vals in vals_list:
            if vals.get("name" , 'New') =='New':
                vals['name']=self.env['ir.sequence'].next_by_code("lab.reservation")

        return super().create(vals_list)




