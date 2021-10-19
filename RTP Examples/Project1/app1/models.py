from django.db import models


class PersonModel(models.Model):

    gender_choices = (('Male','Male'),
                      ('Female','Female'),
                      ('Others','Others'))

    number = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    gender = models.CharField(max_length=10,choices=gender_choices)
    age = models.IntegerField()
    contact = models.IntegerField(unique=True)
    email = models.EmailField(max_length=100,unique=True)
    location = models.CharField(max_length=100)
    profession = models.CharField(max_length=100)
    created_date = models.DateField(auto_now_add=True)

    def __str__(self):
        #full_name = self.first_name+" "+self.last_name
        #return full_name
        return str(self.number)

    # def save(self, *args,**kwargs):
    #     pass


class Students(models.Model):
    name = models.CharField(max_length=100)