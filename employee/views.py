from django.shortcuts import render, redirect  
from employee.forms import EmployeeForm  
from employee.models import Employee  

from employee.forms import CustomerForm  
from employee.models import Customer  

# Create your views here.  
def emp(request, id):  
    if id == 0:
        if request.method == "POST":  
        form = CustomerForm(request.POST)  
        if form.is_valid():  
            try:  
                form.save()  
                return redirect('/show/0')  
            except:  
                pass  
        else:  
            form = CustomerForm()  
        return render(request,'customer/index.html',{'form':form})  
    else:
        if request.method == "POST":  
            form = EmployeeForm(request.POST)  
            if form.is_valid():  
                try:  
                    form.save()  
                    return redirect('/show/0')  
                except:  
                    pass  
        else:  
            form = EmployeeForm()  
        return render(request,'index.html',{'form':form})  
def front(request):  
    return render(request,"front.html")  
def show(request, id):
    if id == 0: # Customer
        customers = Customer.objects.all()
        return render(request, "customer/show.html", {'customer':customers})
    else:
        employees = Employee.objects.all()  
        return render(request,"show.html",{'employees':employees})  
def edit(request, id):  
    employee = Employee.objects.get(id=id)  
    return render(request,'edit.html', {'employee':employee})  
def update(request, id):  
    employee = Employee.objects.get(id=id)  
    form = EmployeeForm(request.POST, instance = employee)  
    if form.is_valid():  
        form.save()  
        return redirect("/show")  
    return render(request, 'edit.html', {'employee': employee})  
def destroy(request, id):  
    employee = Employee.objects.get(id=id)  
    employee.delete()  
    return redirect("/show")  

