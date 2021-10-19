"""Project4_Provider URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.views.generic import ListView

from app_Provider import views
from app_Provider.models import EmployeeModel

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',ListView.as_view(template_name='all_employees.html',model=EmployeeModel)),
]
endpoint_urls = [
    path('view_all_employees/',views.view_all_Employees,name='view_all_employees'),
    path('view_one_employee/<int:emp_id>/',views.view_one_Employee,name='view_one_employee'),
    path('add_one_employee/',views.addoneEmployee,name='add_one_employee'),
    path('update_employee/<int:emp_id>/',views.updateEmployee,name='update_employee'),
    path('delete_employee/<int:emp_id>/',views.deleteEmployee,name='delete_employee'),
]

urlpatterns = urlpatterns + endpoint_urls
