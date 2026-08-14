{
    'name':'Lab Reservation',
    'depends':['base' ],
    'application': True,
    'data': [
        'views/lab_room_views.xml',
        'views/lab_type_views.xml',
        'views/menus.xml',
        'security/ir.model.access.csv',
       
    ]
}