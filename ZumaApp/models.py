from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Signin(models.Model):
    username = models.CharField(max_length=50)
    email_address = models.CharField(max_length=64)
    password = models.CharField(max_length=64)
    
    def __str__(self):
        return f"{self.id} - {self.username} "

# class Signin(models.Model):
#     email_address = models.CharField(max_length=64)
#     password = models.CharField(max_length=64)
    
#     def __str__(self):
#         return f"{self.id} - {self.username} "

class Index(models.Model):
    upload = models.ImageField(null= True, blank=True, upload_to="images/digi.jpeg")
    price = models.IntegerField()
    def __str__(self):
        return f"{self.id} - {self.upload} costs {self.price}  EUR"

