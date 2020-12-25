from django.shortcuts import render, redirect  
from employee.forms import EmployeeForm  
from employee.models import Employee  

from employee.forms import CustomerForm  
from employee.models import Customer  

# Create your views here.  
def emp(request):  
    if request.method == "POST":  
        form = EmployeeForm(request.POST)  
        if form.is_valid():  
            try:  
                form.save()  
                return redirect('/show')  
            except:  
                pass  
    else:  
        form = EmployeeForm()  
    return render(request,'index.html',{'form':form})  
def empProduct(request):  
    if request.method == "POST":  
        form = ProductForm(request.POST)  
        if form.is_valid():  
            try:  
                form.save()  
                return redirect('show/product')  
            except:  
                pass  
    else:  
        form = ProductForm()  
    return render(request,'product/index.html',{'form':form}) 

def empCustomer(request):  
    if request.method == "POST":  
        form = CustomerForm(request.POST)  
        if form.is_valid():  
            try:  
                form.save()  
                return redirect('show/customer')  
            except:  
                pass  
    else:  
        form = CustomerForm()  
    return render(request,'customer/index.html',{'form':form}) 

def empTransaction(request):  
    if request.method == "POST":  
        form = TransactionForm(request.POST)  
        if form.is_valid():  
            try:  
                form.save()  
                return redirect('show/transaction')  
            except:  
                pass  
    else:  
        form = TransactionForm()  
    return render(request,'transaction/index.html',{'form':form}) 

def front(request):  
    return render(request,"front.html")  
def show(request):
    employees = Employee.objects.all()  
    return render(request,"show.html",{'employees':employees})  

def showCustomer(request):
    customers = Customer.objects.all()  
    return render(request,"customer/show.html",{'customers':customers})  

def showTransaction(request):
    transactions = Transaction.objects.all()  
    return render(request,"transaction/show.html",{'transactions':transactions})  

def showProduct(request):
    products = Product.objects.all()  
    return render(request,"product/show.html",{'products':products})  

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

