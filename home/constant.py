

class ROLE_CHOICES:
    CUSTOMER='Customer'
    OWNER='Owner'

    CHOICES=[
    
        (CUSTOMER,'Customer'),
        (OWNER,'Owner'),
    ]

class VEHICLE_TYPE:
    SEDAN='Sedan'
    SUV='Suv'
    VAN='Van'
    TRUCK='Truck'
    CONVERTIBLE='Convertible'

    CHOICES=[
        (SEDAN,'Sedan'),
        (SUV,'Suv'),
        (VAN,'Van'),
        (TRUCK,'Truck'),
        (CONVERTIBLE,'Convertible')
    ]
class TRANSMISSION_TYPE:
   
    AUTOMATIC = 'Automatic'
    MANUAL = 'Manual'

    CHOICES = [
        (AUTOMATIC, 'Automatic'),  
        (MANUAL, 'Manual'),
    ]