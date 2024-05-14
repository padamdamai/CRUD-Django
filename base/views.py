from django.shortcuts import render, redirect
from .models import *

def home(request):
    employ = Employees.objects.all()
    context = {
        'emp':employ,
    }
    return render(request,'base/home.html',context)
    