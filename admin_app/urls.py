
from django.urls import path
from . import views
app_name="admin_app"
urlpatterns = [
    path('', views.index,name="index"),
    path('<int:id>/',views.getUserDetail,name='user_detail'),
    path("/logout",views.signout,name="logout"),
]