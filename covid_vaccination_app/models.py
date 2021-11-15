from django.db import models
from django.db.models.deletion import CASCADE
from django.contrib.auth.models import User
# Create your models here.
class District(models.Model):
    district_name=models.CharField(max_length=150)
    state=models.CharField(max_length=150)
    
    def __str__(self):
        return self.district_name
    class Meta:
        ordering=['district_name']
class Place(models.Model):
    place_name=models.CharField(max_length=150)
    district=models.ForeignKey(District,on_delete=CASCADE)
    def __str__(self):
        return self.place_name
    class Meta:
        ordering=['place_name']
    
class VaccinationBooking(models.Model):
    vaccination_token_id=models.CharField(max_length=150)
    phone_number=models.CharField(max_length=20)
    date_of_birth=models.DateField()
    gender=models.CharField(max_length=15)
    covid_affected=models.CharField(max_length=5)
    symptoms=models.CharField(max_length=250)
    address=models.TextField()
    district=models.CharField(max_length=100)
    place=models.CharField(max_length=150)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    def __str__(self):
        return '{}'.format(self.user)