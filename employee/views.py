from django.shortcuts import render, redirect  
from employee.forms import EmployeeForm  
from employee.models import Employee  

from employee.forms import CustomerForm  
from employee.models import Customer  

from employee.forms import TransactionForm  
from employee.models import Transaction  

from employee.forms import ProductForm
from employee.models import Product

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
                return redirect('/show/product')  
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
                return redirect('/show/customer')  
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
                return redirect('/show/transaction')  
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

def editProduct(request, id):  
    product = Product.objects.get(productID=id)  
    return render(request,'/product/edit.html', {'product':product})  

def editCustomer(request, name):  
    customer = Employee.objects.get(name=name)  
    return render(request,'/customer/edit.html', {'customer':customer})  

def editTransaction(request, transactionNumber):  
    transaction = Transaction.objects.get(transactionNumber=transactionNumber)  
    return render(request,'/transaction/edit.html', {'transaction':transaction})  

def update(request, id):  
    employee = Employee.objects.get(id=id)  
    form = EmployeeForm(request.POST, instance = employee)  
    if form.is_valid():  
        form.save()  
        return redirect("/show")  
    return render(request, 'edit.html', {'employee': employee})  

def updateProduct(request, id):  
    product = Product.objects.get(productID=id)  
    form = ProductForm(request.POST, instance = product)  
    if form.is_valid():  
        form.save()  
        return redirect("/show/product")  
    return render(request, '/product/edit.html', {'product': product})  

def updateCustomer(request, name):  
    customer = Customer.objects.get(name=name)  
    form = CustomerForm(request.POST, instance = customer)  
    if form.is_valid():  
        form.save()  
        return redirect("/show/customer")  
    return render(request, '/customer/edit.html', {'customer': customer})  

def updateTransaction(request, transactionNumber):  
    transaction = Transaction.objects.get(transactionNumber=transactionNumber)  
    form = TransactionForm(request.POST, instance = transaction)  
    if form.is_valid():  
        form.save()  
        return redirect("/show/transaction")  
    return render(request, '/transaction/edit.html', {'transaction': transaction})  

def destroy(request, id):  
    employee = Employee.objects.get(id=id)  
    employee.delete()  
    return redirect("/show")  

def destroyProduct(request, id):  
    product = Product.objects.get(productID=id)  
    product.delete()  
    return redirect("/show/product")  

def destroyCustomer(request, name):  
    customer = Customer.objects.get(name=name)  
    customer.delete()  
    return redirect("/show/customer")  

def destroyTransaction(request, transactionNumber):  
    transaction = Transaction.objects.get(transactionNumber=transactionNumber)  
    transaction.delete()  
    return redirect("/show/transaction")  

def csvUpload(request):  
    if request.method == "POST":  
        for filename, csv_file in request.FILES.items():
            if not csv_file.name.endswith('.csv'):
                continue
            name = request.FILES[filename].name
            file_data  = csv_file.read().decode("utf-8")
            lines = file_data.split("\n")
            #loop over the lines and save them in db. If error , store as string and then display
            for line in lines:
                fields = line.split(",")
                dataType = fields[0]
                data = {}
                if dataType == 'C': # Customer
                    data["name"] = fields[1].lstrip()
                    data["phone"] = fields[2].lstrip()
                    data["address"] = fields[3].lstrip()
                    data["gender"] = fields[4].lstrip().replace('\r', '')

                    form = CustomerForm(data)
                    if form.is_valid():  
                        try:  
                            form.save()  
                        except:  
                            pass 
                
                elif dataType == 'P': # Product
                    data["name"] = fields[1].lstrip()
                    data["productID"] = fields[2].lstrip()
                    data["supplierName"] = fields[3].lstrip().replace('\r', '')

                    form = ProductForm(data)
                    if form.is_valid():  
                        try:  
                            form.save()   
                        except:  
                            pass
                elif dataType == 'T': # Transaction
                    data["transactionNumber"] = fields[1].lstrip()
                    data["productID"] = fields[2].lstrip()
                    data["price"] = fields[3].lstrip()
                    data["date"] = fields[4].lstrip()
                    data["customerName"] = fields[5].lstrip().replace('\r', '')

                    form = TransactionForm(data)
                    if form.is_valid():  
                        try:  
                            form.save()    
                        except:  
                            pass
                #print(data)
                
                
        return render(request, 'front.html')
    else:  
        return render(request,'csvUpload.html',)  
    
def search(request):  
    print(request.POST)
    customers = Customer.objects.all() 
    return render(request,"customer/show.html",{'customers':customers})  
