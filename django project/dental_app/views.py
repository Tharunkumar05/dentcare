from django.shortcuts import redirect, get_object_or_404,render
from django.http import HttpResponse, HttpResponseRedirect
from dental_app.form import CustomUserForm
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from .models import Registration
from django.urls import reverse
from django.http import JsonResponse
import json


def list(request):
    if request.headers.get('x-requested-with')=='XMLHttpRequest':
        if request.user.is_authenticated:
            data=json.load(request)
            return JsonResponse({'status':'Appointment Registered Successfully'},status=200)
    else:
        return JsonResponse({'status':'Invalid Access'},status=200)
# 
def delete(request, id):
    app = get_object_or_404(Registration, id=id, user=request.user)
    app.delete()
    return HttpResponseRedirect(reverse('schedule-page'))


def schedule(request):
    sch = Registration.objects.filter(user=request.user)
    return render(request, "challeneges\schedule.html",{"sch":sch})


def login_page(request):
    if request.method == 'POST':
        name = request.POST.get('username')
        pwd = request.POST.get('password')
        user=authenticate(request,username=name,password=pwd)
        if user is not None:
            login(request,user)
            messages.success(request,"Logged in Successfully")
            return HttpResponseRedirect("home")
        else:
            messages.error(request,"Invalid User Name or Password")
            return HttpResponseRedirect("login")
    return render(request, "challeneges\login.html")


def logout_page(request):
    if request.user.is_authenticated:
        logout(request)
        messages.success(request,"Logged out Successfully")
    return HttpResponseRedirect("home")

def home(request):
    return render(request, "challeneges\home.html")


def service(request):
    return render(request, 'challeneges\service.html')



def signup(request):
    form = CustomUserForm
    if request.method == 'POST':
        form=CustomUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Registration Success You can Login Now...!")
            return HttpResponseRedirect("login")
    return render(request,"challeneges\signup.html",{'form':form})
    
    #     if request.POST['name'] == '':
    #         return render(request, "challeneges\signup.html", {"has-error": True})
    #     elif request.POST['email'] == '':
    #         return render(request, "challeneges\signup.html", {"has-error": True})
    #     elif request.POST['phone'] == '':
    #         return render(request, "challeneges\signup.html", {"has-error": True})
    #     elif request.POST['pwd'] == '':
    #         return render(request, "challeneges\signup.html", {"has-error": True})
    #     elif request.POST['pwd1'] == '':
    #         return render(request, "challeneges\signup.html", {"has-error": True})
    #     return HttpResponseRedirect("login")
    # return render(request, "challeneges\signup.html", {"has-error": False})

@login_required
def book(request):
    if request.method=='POST':
        date=request.POST.get('registration_date')
        name=request.POST.get('patient_name')
        gen=request.POST.get('gender')
        phone=request.POST.get('phone_number')
        email=request.POST.get('email')
        city=request.POST.get('city')
        user=request.user.id
        reg=Registration(registration_date=date, patient_name=name,gender=gen,phone_number=phone,email=email,city=city,user_id=user)
        reg.save()
        return HttpResponseRedirect('schedule')
    return render(request, 'challeneges/book.html')


def about(request):
    return render(request, "challeneges/about.html")
