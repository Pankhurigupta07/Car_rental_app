from django.db import models
from home.constant import ROLE_CHOICES,VEHICLE_TYPE,TRANSMISSION_TYPE

class BaseModel(models.Model):
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract=True


class UserProfile(models.Model):
    user=models.OneToOneField('auth.User',on_delete=models.CASCADE)
    role=models.CharField(max_length=50, choices=ROLE_CHOICES.CHOICES)
    phone=models.CharField(max_length=15, unique=True)
    address=models.TextField()

class Vehicle(BaseModel):
    owner=models.ForeignKey(UserProfile,on_delete=models.CASCADE)
    title=models.CharField(max_length=100)
    description=models.TextField()
    city=models.CharField(max_length=50)
    location=models.CharField(max_length=100)
    pickup_location=models.CharField(max_length=100)
    Vehicle_type=models.CharField(max_length=100,choices=VEHICLE_TYPE.CHOICES)
    make=models.CharField(max_length=50,null=True,blank=True)
    model=models.CharField(max_length=50,null=True,blank=True)
    transmission=models.CharField(max_length=50,choices=TRANSMISSION_TYPE.CHOICES)
    hourly_rate=models.DecimalField(max_digits=10,decimal_places=2)
    daily_rate=models.DecimalField(max_digits=10,decimal_places=2)
    weekly_rate=models.DecimalField(max_digits=10,decimal_places=2)
    is_active=models.BooleanField(default=True)
    created_at=models.DateTimeField(auto_now_add=True)

class VehicleImage(BaseModel):
    Vehicle=models.ForeignKey(Vehicle,on_delete=models.CASCADE)
    Image=models.ImageField(upload_to='vehicle_image/')