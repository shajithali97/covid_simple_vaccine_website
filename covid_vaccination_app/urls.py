
from django.urls import path
from . import views
app_name="covid_app"
urlpatterns = [
    path('', views.index,name="index"),
    path('login/',views.login,name="login"),
    path('registration/',views.registration,name="registration"),
    path('booking/',views.booking_slot,name="booking_slot"),
     path('ajax/load-cities/', views.load_cities, name='ajax_load_cities'),   
]
