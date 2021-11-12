from django.shortcuts import render,redirect
from customer.models import *
#from customer.forms import CustomerForm


# will redirect to main page.
def showIndex(request):
    return render(request,'index.html')


def showCategory(request):
    return render(request, "customer/view_category.html",{"categories":Category.objects.order_by('cat_name')})


def showFood(request):
    return render(request, "customer/view_food.html",{"foods":Food.objects.order_by('item_name')})


def customerLogin(request):
      if request.method == "POST":
          email = request.POST.get('email')
          password = request.POST.get('password')
          try:
            cm = Customer.objects.get(Customer_email=email,Customer_password=password)
            return render(request,"customer/welcomepage.html",{"user":Customer.objects.get(Customer_email=email)})
          except Customer.DoesNotExist:
              return render(request,"customer/login.html",{"error":"Sorry Invalid User.!!! Please Register Your Self"})
      else:
          return render(request,"customer/login.html")


def customerRegister(request):
      if request.method == "POST":
          name = request.POST.get("Customer_name")
          contact = request.POST.get("Customer_contact")
          email = request.POST.get("Customer_email")
          password = request.POST.get("Customer_password")
          address = request.POST.get("Customer_address")

          record = Customer(Customer_name=name,Customer_contact=contact,Customer_email=email,Customer_password=password,Customer_address=address).save()
          return render(request,"customer/registation.html",{"message":'Thanks For Registration'})
      else:
          return render(request,"customer/registation.html")


def customerWelcome(request):
    return render(request, 'customer/welcomepage.html')


def displayUser(request):
        return render(request,"customer/displayuser.html")