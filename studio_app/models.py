from datetime import datetime
from django.db import models

# Create your models here
class Lab(models.Model):       
    name= models.CharField(max_length = 100, null = False, blank = False)

    class Meta:
        verbose_name_plural = 'Labs'


    def __str__(self):
     return self.name

class Component(models.Model):     
    lab = models.ForeignKey( Lab,on_delete=models.PROTECT)  
    name = models.CharField(max_length = 100, null = False , blank= False)
    value = models.CharField(max_length = 20, null = False, blank = False)
    quantity = models.PositiveIntegerField(null = False, blank = False, default = 0 )
    cost =models.IntegerField(null = False, blank = False, default = 0 )

    class Meta:
        verbose_name_plural = 'Components'


    def __str__(self):
     return self.name


class Source_of_Income(models.Model):       
    name = models.CharField(max_length = 100, null = False, blank = False )

    class Meta:
        verbose_name_plural = 'Source-of-Income'


    def __str__(self):
     return self.name


class Income(models.Model): 
    name = models.ForeignKey(Source_of_Income, on_delete = models.PROTECT)  
    lab = models.ForeignKey(Lab, on_delete = models.PROTECT)  
    amount = models.FloatField(null = False, blank = False, default = 0 ) 
    description = models.CharField(max_length = 1000, null = True ,blank = True)
    date = models.DateField(null = False, blank = False, default = datetime.now())  

    class Meta:
        verbose_name_plural = 'Income'


    def __str__(self):
     return self.name  

class Purchases(models.Model):
    lab = models.ForeignKey(Lab, on_delete = models.PROTECT)
    component =models.ForeignKey(Component, on_delete = models.PROTECT)
    quantity = models.PositiveIntegerField(null = False, blank = False)
    amount = models.FloatField(null = True, blank = True)
    date= models.DateField(null = False, blank = False)  

    class Meta:
        verbose_name_plural = 'Purchases'


    def __str__(self):
     return self.lab.name  

class Source_Of_Expenses(models.Model):
    name = models.CharField(max_length = 255, null = False, blank = False)

    class Meta:
        verbose_name_plural = 'Source-Of-Expenses'


    def __str__(self):
     return self.name

class Expenses(models.Model):
    name = models.ForeignKey(Source_Of_Expenses, on_delete =models.PROTECT)
    lab = models.ForeignKey(Lab, on_delete = models.PROTECT)
    amount = models.FloatField(null = False, blank = False)
    date = models.DateField(null = False, blank = False)

    class Meta:
        verbose_name_plural = 'Expenses'


    def __str__(self):
     return self.name
    
class Member_type(models.Model):
   type =  models.CharField(max_length=255)

   class Meta:
        verbose_name_plural = 'Member Type'


   def __str__(self):
     return self.type

class Location(models.Model):
   name =  models.CharField(max_length=255)

   class Meta:
        verbose_name_plural = 'Location'


   def __str__(self):
     return self.name

class Member(models.Model):
    #gender choices.
    CHOICES = (
                ('male', 'male'),
               ('female','female'),
               )
    type = models.ForeignKey(Member_type,on_delete = models.PROTECT )
    location = models.ForeignKey(Location,on_delete = models.PROTECT )
    firstName = models.CharField(max_length = 255, blank = False, null = False)
    middleName = models.CharField(max_length = 255, blank = True, null = True)
    lastName = models.CharField(max_length = 255, blank = False, null = False)
    dateOfBirth = models.DateField(null = False, blank = False)
    registrationNumber = models.CharField(max_length = 255, blank = False, null = False)
    phoneNumber = models.CharField(max_length = 255, blank = False, null = False)
    email = models.EmailField(null = False, blank = False)
    idNumber = models.CharField(max_length = 255, blank = False, null = False)
    registeredDate = models.DateField(null = True, blank = False)
    nationality = models.CharField(max_length=255, blank = False, null = False)
    gender = models.CharField(max_length=255, choices = CHOICES,null = False, blank = False)

    class Meta:
        verbose_name_plural = 'Students'


    def __str__(self):
     return f'{self.firstName}  {self.lastName}'
