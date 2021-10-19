from django.contrib import admin
from app1.models import PersonModel

from mlxtend.classifier import StackingClassifier




from django.db.models import Avg
from django.db.models import Max
from django.db.models import Min
from django.db.models import Sum
from django.db.models import Count



#admin.site.register(PersonModel)


@admin.register(PersonModel)
class PersonAdmin(admin.ModelAdmin):
    list_display = ('number','first_name','last_name','gender','age','contact','email','location','profession','created_date')



