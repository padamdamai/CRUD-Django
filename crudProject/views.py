from django.shortcuts import render,redirect
from base.models import Employees

def INDEX(request):
    emp = Employees.objects.all()
    # print(emp)
    context = {
        "emp " : emp,
    }
    return render(request,'index.html',context)


