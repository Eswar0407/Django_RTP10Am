"""Project6 URL Configuration

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

from app6 import views

urlpatterns = [
    path('admin/', admin.site.urls),


    #End Application
    path('add_employee/',views.addEmployee,name='add_employee'),
    path('all_employees/',views.AllEmployees.as_view(),name='all_employees'),
    path('view_one_employee/',views.Employee.as_view()),
    path('view_all_employees/',views.Employee.as_view()),

]
