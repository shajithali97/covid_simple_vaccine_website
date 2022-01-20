from django.http.response import HttpResponse
from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import messages, auth
from covid_vaccination_app import views
# Create your views here.
def login(request):
    if request.method == "POST":
        username=request.POST['user_name']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            if user.is_superuser:
               return redirect('admin_app:index')
            else:
                return redirect('covid_app:index')
            # try:
            #     us=User.objects.get(category = 'admin') 
            #     if us:
            #         return redirect('admin:index')    
            # except Exception as e:     
            #         # return render(request, 'main/home.html') 
            #         return redirect('covid_app:index')
            # print("LOGGED")
            
        else:
            messages.info(request,"INVALID CREDIENTIALS")
            return redirect('covid_app:login')
    return views.login(request)
def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        c_password = request.POST['confirm_password']
        
        if password == c_password:
            if User.objects.filter(username=username).exists():
                messages.info(request, "USERNAME TAKEN")
                return redirect('covid_app:registration')
            elif User.objects.filter(email=email).exists():
                messages.info(request, "EMAIL TAKEN")
                return redirect('covid_app:registration')
            else:
                user = User.objects.create_user(username=username, email=email, password=password,
                                                first_name=first_name,
                                                last_name=last_name)
                user.save()
            print("USER CREATED")
        else:
            messages.info(request, "PASSWORD NOT MATCH")
            return redirect('covid_app:registration')
            # print("PASSWORD NOT MATCH")
        return redirect('covid_app:login')
    return render(request, 'register.html')
def logout(request):
    auth.logout(request)
    return redirect('/')
