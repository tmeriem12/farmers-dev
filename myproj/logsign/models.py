from django.db import models
# Create your models here.
class Clinique(models.Model):
    name=models.CharField('clinique name' , max_length=120)
    adress=models.CharField('adress', max_length=200)
    description=models.CharField('clinique desc' , max_length=200 , blank=False)
    '''doctors= '''liste''''''''
    phone=models.IntegerField()

class Patient(models.Model):
    name=models.CharField('patient name',max_length=120)
    lastname=models.CharField('patient name')


