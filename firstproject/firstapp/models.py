from django.db import models

# Create your models here.


class Login(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField(max_length=30, unique=True)
    password = models.CharField(max_length=20)