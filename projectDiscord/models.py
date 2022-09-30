from unittest.util import _MAX_LENGTH
from django.db import models

""" Modelando la Base de Datos de Master Bot """



class User(models.Model):
    name = models.CharField(max_length=30)
    lastname = models.CharField(max_length=30)
    email = models.EmailField(max_length=30)
    password = models.CharField(max_length=30)
    remember_password = models.CharField(max_length=100)


class Bot(models.Model):
    name = models.CharField(max_length=30)
    token = models.CharField(max_length=30)
    welcome_message = models.TextField(300)
    user = models.ForeignKey(User, on_delete=models.CASCADE) 
    


