from django.db import models



# Create your models here.
class Sign_in(models.Model):
    username=models.CharField(max_length=50)
    email=models.EmailField(max_length=50)
    password1=models.CharField(max_length=50)

class login(models.Model):
    username=models.CharField(max_length=50)
    password1=models.CharField(max_length=50)
class Index(models.Model):
    placename=models.CharField(max_length=50)
    image=models.ImageField(upload_to="static/admin/img/")



