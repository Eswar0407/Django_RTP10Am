from django.contrib import admin
from app_Provider.models import EmployeeModel

# Register your models here.

@admin.register(EmployeeModel)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['idno','name','salary']
    list_filter = ['name']