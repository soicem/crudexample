"""crudexample URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from employee import views  
urlpatterns = [  
    path('admin/', admin.site.urls),  
    path('', views.front),
    path('emp/', views.emp),  
    path('emp/product',views.empProduct),  
    path('emp/customer',views.empCustomer),
    path('emp/transaction',views.empTransaction),
    path('show/product',views.showProduct),  
    path('show/customer',views.showCustomer),
    path('show/transaction',views.showTransaction),
    path('show',views.show),  
    path('edit/<int:id>', views.edit),
    path('edit/product/<int:id>', views.editProduct), 
    path('edit/customer/<int:id>', views.editCustomer), 
    path('edit/transaction/<int:id>', views.editTransaction),   
    path('update/<int:id>', views.update),  
    path('update/product/<int:id>', views.updateProduct),
    path('update/customer/<int:id>', views.updateCustomer),
    path('update/transaction/<int:id>', views.updateTransaction),
    path('delete/<int:id>', views.destroy),  
    path('delete/product/<int:id>', views.destroyProduct),  
    path('delete/customer/<int:id>', views.destroyCustomer),  
    path('delete/transaction/<int:id>', views.destroyTransaction),  
    path('CSVUpload/', views.csvUpload),
    path('searchCustomer/', views.searchCustomer),
    path('searchTransaction/', views.searchTransaction),
    path('searchProduct/', views.searchProduct),
    path('specialSearch/', views.specialSearch),
    path('searchK/', views.searchK),
    path('searchM/', views.searchM),
    path('deleteAll/', views.deleteAll)
]  
