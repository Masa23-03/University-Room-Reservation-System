{
    'name':'Lab Reservation',
    'depends':['base' ],
    'application': True,
    'data': [
        'security/lab_reservation_groups.xml',
        'security/ir.model.access.csv',
        'data/lab_reservation_sequence.xml',
        'views/lab_room_views.xml',
        'views/lab_type_views.xml',
        'views/lab_requirement_views.xml',
        'views/lab_reservation_requester_views.xml',
        'views/menus.xml',
        
       
    ]
}