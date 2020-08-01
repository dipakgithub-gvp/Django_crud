from django.shortcuts import render, HttpResponse, redirect
from .models import EmployeeDetails
from django.contrib import messages

# Create your views here.

def index(request):
    all_data = EmployeeDetails.objects.all()
    employees = {'all_data':all_data}
    return render(request,"crud/index.html",employees)


def insert_data(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        address = request.POST['address']
        phone = request.POST['phone']
        image = request.FILES['image_file']
        if(name==''or email==''or address==''or phone==''):
            messages.warning(request,"Please fill form Correctly..!")
        else:
            emp = EmployeeDetails(name=name, email=email, phone=phone, address=address,image=image)
            emp.save()
            messages.success(request,"Data inserted Successfully..!")
    return redirect(index)
    # return render(request,"crud/index.html")

def update_data(request,id):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        address = request.POST['address']
        phone = request.POST['phone']
        image = request.FILES['image_file']

        if(name==''or email==''or address==''or phone==''):
            messages.warning(request,"Please fill form Correctly..!")
        else:
            emp = EmployeeDetails(name=name, email=email, phone=phone, address=address,image=image,id=id)
            emp.save()
            messages.success(request,"Data updated Successfully..!")
    return redirect(index)


def delete_data(request,id):
    if request.method == "GET":
        get_data = EmployeeDetails.objects.filter(id=id)
        get_data.delete()
        messages.error(request, 'Data deleted successfully..!')
    return redirect(index)
