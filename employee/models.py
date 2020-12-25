from django.db import models  
class Employee(models.Model):  
    eid = models.CharField(max_length=20)  
    ename = models.CharField(max_length=100)  
    eemail = models.EmailField()  
    econtact = models.CharField(max_length=15)  
    class Meta:  
        db_table = "employee" 

class Customer(models.Model):  
    name = models.CharField(max_length=100, primary_key=True)  
    phone = models.CharField(max_length=30)  
    address = models.CharField(max_length=15)  
    gender = models.CharField(max_length=15)  
    class Meta:  
        db_table = "customer" 

class Product(models.Model):  
    name = models.CharField(max_length=100)  
    productID = models.CharField(max_length=100, primary_key=True)  
    supplierName = models.CharField(max_length=30)
    class Meta:  
        db_table = "product" 

class Transaction(models.Model):  
    transactionNumber = models.CharField(max_length=100, primary_key=True)  
    productID = models.ForeignKey("Product", on_delete=models.CASCADE) 
    price = models.CharField(max_length=30)  
    date = models.DateTimeField()
    custmerName = models.CharField(max_length=100)  
    class Meta:  
        db_table = "transaction" 



