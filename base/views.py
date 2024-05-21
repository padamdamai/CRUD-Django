from django.shortcuts import render, redirect
from .models import *

def home(request):
    employ = Employees.objects.all()
    context = {
        'emp':employ,
    }
    return render(request,'base/home.html',context)

def add(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        address = request.POST.get('address')
        phone = request.POST.get('phone')

        emp = Employees(
            name= name,
            email= email,
            address = address,
            phone = phone,

        )
        emp.save()
        return redirect('home')

    return render(request,'base/home.html')

def Edit(request):
    emp = Employees.objects.all()
    context = {
        'emp':emp,
    }
    return redirect(request,'base/home.html',context)

def Update(request,id):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        address = request.POST.get('address')
        phone = request.POST.get('phone')
        
        emp = Employees(
            id = id,
            name = name,
            email = email,
            address = address ,
            phone = phone
        )
        emp.save()
        return redirect('home')
        

    return redirect(request,'base/home.html')

def Delete(request,id):
    emp = Employees.objects.filter(id=id).delete()

    return redirect('home')
