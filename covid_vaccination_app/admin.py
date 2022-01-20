from django.contrib import admin
from .models import District,Place,VaccinationBooking
# Register your models here.
admin.site.register(District)
admin.site.register(Place)
admin.site.register(VaccinationBooking)