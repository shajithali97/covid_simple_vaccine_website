from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.urls import reverse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from credentials.views import logout
from covid_vaccination_app.models import Place,District,VaccinationBooking
# Create your views here.
def index(request):
    
    user=User.objects.all().filter(is_superuser=False)
    page = request.GET.get('page', 1)
    paginator = Paginator(user, 10)
    try:
        users = paginator.page(page)
    except PageNotAnInteger:
        users = paginator.page(1)
    except EmptyPage:
        users = paginator.page(paginator.num_pages)

    return render(request,"admin.html",{"users":users})
def getUserDetail(request,id):
    user=VaccinationBooking.objects.get(user=id)
    
    return render(request,'user_details.html',{"selected_user":user})
    
def signout(request):
    logout(request)
    return redirect(reverse('covid_app:index'))