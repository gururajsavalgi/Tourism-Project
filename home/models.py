from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator



# Create your models here.
class Sign_in(models.Model):
    username=models.CharField(max_length=50)
    email=models.EmailField(max_length=50)
    password1=models.CharField(max_length=50)

class login(models.Model):
    username=models.CharField(max_length=50)
    password=models.CharField(max_length=50)
class Index(models.Model):
    place_id = models.AutoField
    placename=models.CharField(max_length=50)
    category = models.CharField(max_length=50, default="")
    subcategory = models.CharField(max_length=50, default="")
    price = models.IntegerField(default=0)
    description=models.TextField(default="")
    image=models.ImageField(upload_to="static/admin/img/", default="")
    image1=models.ImageField(upload_to="static/admin/img/", default="")
    image2=models.ImageField(upload_to="static/admin/img/", default="")
    
    def __str__(self):
        return self.placename
class Contact(models.Model):
    msg_id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=50)
    email=models.EmailField(max_length=70, default="")
    phone=models.CharField(max_length=50, default="")
    desc=models.CharField(max_length=300, default="")
    def __str__(self):
        return self.name
class Customer_detail(models.Model):
    msg_id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=50)
    phone=models.CharField(max_length=50, default="")
    def __str__(self):
        return self.name


class Guide_detail(models.Model):
    msg_id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=50)
    phone=models.CharField(max_length=50, default="")
    rating = models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(5)])
    def __str__(self):
        return self.name


