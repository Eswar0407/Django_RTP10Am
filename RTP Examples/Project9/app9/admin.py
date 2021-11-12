from django.contrib import admin
from app9.models import Category,Food
from django.contrib.auth.models import Group,User

# Register your models here.
admin.site.unregister(Group)
admin.site.unregister(User)

@admin.register(Category)
class AdminCategory(admin.ModelAdmin):
    list_display=['cat_id','cat_name']


@admin.register(Food)
class AdminFood(admin.ModelAdmin):
    list_display=['item_id','item_name','item_price','item_photo','item_status','cat_id']
