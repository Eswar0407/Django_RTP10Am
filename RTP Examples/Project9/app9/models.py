from django.db import models

class Category(models.Model):
    cat_id = models.AutoField(primary_key=True)
    cat_name = models.CharField(max_length=30,unique=True)

    def __str__(self):
       return self.cat_name


class Food(models.Model):
    item_id = models.AutoField(primary_key=True)
    item_name = models.CharField(max_length=30)
    item_price = models.FloatField()
    item_photo = models.ImageField(upload_to="food_images/")
    item_status = models.CharField(max_length=50)
    cat_id = models.ForeignKey(Category,on_delete=models.CASCADE)

class Customer(models.Model):
    cust_id = models.AutoField(primary_key=True)
    cust_name = models.CharField(max_length=30)
    cust_contact = models.IntegerField(unique=True)
    cust_email = models.EmailField(max_length=30,unique=True)
    cust_password = models.CharField(max_length=30)
    cust_address = models.TextField()


class Order(models.Model):
    order_id = models.AutoField(primary_key=True)
    order_date = models.DateField(auto_now_add=True)
    order_time = models.TimeField(auto_now_add=True)
    cust_id = models.ForeignKey(Customer,on_delete=models.CASCADE)


class Quantity(models.Model):
    quantity_no = models.AutoField(primary_key=True)
    ord_id = models.ForeignKey(Order,on_delete=models.CASCADE)
    food_id = models.ForeignKey(Food,on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()