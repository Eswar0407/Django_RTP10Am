
from django.contrib import admin
from django.urls import path

from ProjectOFO_9 import settings
from customer import views
from django.conf.urls.static import static

urlpatterns = [
         path('',views.showIndex,name='index'),
         path('view_category/',views.showCategory,name='view_category'),
         path('view_food/',views.showFood,name='view_food'),
         path('customer_login/',views.customerLogin,name='customer_login'),
         path('customer_register/',views.customerRegister,name='customer_register'),
         path('welcome_page/',views.customerWelcome,name='customer_welcome'),
         path('view_category_food_item/<int:cat_id>/',views.viewcategoryFooditem,name='view_category_food_item'),
         path('contact_us/',views.contactUs,name='contact_us'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
