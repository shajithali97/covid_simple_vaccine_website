from django.shortcuts import render
from . models import Place,District,VaccinationBooking
from django.http import JsonResponse,HttpResponse
from django.contrib.auth.models import User
# Create your views here.
def index(request):
    return render(request,'index.html')
def booking_slot(request):
    context={}
    v_id=request.user.id
    if request.method == "POST":
        
        v_b=None
        try:
            
            v_b=VaccinationBooking.objects.get(user_id=v_id)
            print(v_b)
        except:
            v_b=None
            print("error") 
        print(v_b)  
        if v_b == None:
        
            phone_number=request.POST.get('phone_number')
            dob=request.POST.get('dob')
            gender=request.POST.get('gender')
            covid=request.POST.get('covid')
            symptoms = request.POST.getlist('symptoms')
            
            address=request.POST.get('address')
            district=request.POST.get('district')
            place=request.POST.get('place')
            username = request.user.username
            id_user=request.user.id
            vaccination_id=username+phone_number
            vaccination=VaccinationBooking(vaccination_token_id=vaccination_id,phone_number=phone_number,date_of_birth=dob,gender=gender,covid_affected=covid,symptoms=symptoms,address=address,district=district,place=place,user_id=id_user)
            vaccination.save()
            v=VaccinationBooking.objects.get(user_id=v_id)
            return render(request,'booked.html',{'v_id':v,"msg":False})
        else:
            v=VaccinationBooking.objects.get(user_id=v_id)
            return render(request,'booked.html',{'v_id':v,"msg":True})
        return HttpResponse(id_user)
    if request.user.is_authenticated:
        v_b=None
        try:
            
            v_b=VaccinationBooking.objects.get(user_id=v_id)
            print(v_b)
        except:
            v_b=None
            print("error") 
        print(v_b)  
        if v_b == None:
            place=Place.objects.all()
            district=[]
            for d in place:
                district.append(d.district)
            print(list(set(district)))
            context['districts']=list(set(district))
            return render(request,'booking.html',context)
        else:
            v=VaccinationBooking.objects.get(user_id=v_id)
            return render(request,'booked.html',{'v_id':v,"msg":True})
    return login(request)

    
def login(request):
    if request.user.is_authenticated:
        return HttpResponse("Already Login . ")
    return render(request,'login.html')
def registration(request):
    if request.user.is_authenticated:
        return HttpResponse("Already Login . ")
    return render(request,'registration.html')
# AJAX
def load_cities(request):
    select_district = request.GET.get('selectedDistrict')
    print("DIS",select_district)
    get_district_id=District.objects.get(district_name=select_district)
    
    places=list(Place.objects.filter(district=get_district_id.id).values())
    return JsonResponse({"data":places})
    print("DIS",places)
    return HttpResponse(get_district_id)
    cities = City.objects.filter(country_id=country_id).all()
    return render(request, 'persons/city_dropdown_list_options.html', {'cities': cities})
    # return JsonResponse(list(cities.values('id', 'name')), safe=False)

