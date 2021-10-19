from django import forms
from app_Provider.models import EmployeeModel

class EmployeeForm(forms.ModelForm):
    class Meta:
        fields = "__all__"
        model = EmployeeModel

