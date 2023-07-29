from django.db import models

# Create your models here.
class RegisterUser(models.Model):    
    firstName = models.CharField(max_length = 255,unique = False,)       
    lastName = models.CharField(max_length = 255,unique = False,) 
    userName = models.CharField(max_length = 255)
    email = models.EmailField () 
    password = models.CharField(max_length = 16)                        

