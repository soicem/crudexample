from django import forms  
from employee.models import Customer  
from employee.models import Employee
from employee.models import Transaction  
from employee.models import Product
class EmployeeForm(forms.ModelForm):  
    class Meta:  
        model = Employee  
        fields = "__all__"  

class CustomerForm(forms.ModelForm):  
    class Meta:  
        model = Customer  
        fields = "__all__"

class ProductForm(forms.ModelForm):  
    class Meta:  
        model = Product  
        fields = "__all__"

class TransactionForm(forms.ModelForm):  
    class Meta:  
        model = Transaction  
        fields = "__all__"