from distutils.command.upload import upload
from django.db import models

# Create your models here.

class b(models.Model):
    name8=models.CharField(max_length=250)
    img=models.ImageField(upload_to='pics')
    desc=models.TextField
    
    
    def __str__(self):
        return self.name8
class forest(models.Model):
    name2=models.CharField(max_length=250)
    img=models.ImageField(upload_to='pics')
    desc=models.TextField
    
    
    def __str__(self):
        return self.name2
class hillstation(models.Model):
    name3=models.CharField(max_length=250)
    img=models.ImageField(upload_to='pics')
    desc=models.TextField
    
    
    def __str__(self):
        return self.name3


class founder(models.Model):
    name4=models.CharField(max_length=250)
    img=models.ImageField(upload_to='pics')
    desc=models.TextField()
    
    
    def __str__(self):
        return self.name4

class manager(models.Model):
    name5=models.CharField(max_length=250)
    img=models.ImageField(upload_to='pics')
    desc=models.TextField()
    
    
    def __str__(self):
        return self.name5

class travel(models.Model):
    name6=models.CharField(max_length=250)
    img=models.ImageField(upload_to='pics')
    desc=models.TextField()
    
    
    def __str__(self):
        return self.name6

class consultant(models.Model):
    name7=models.CharField(max_length=250)
    img=models.ImageField(upload_to='pics')
    desc=models.TextField()
    
    
    def __str__(self):
        return self.name7
class beach(models.Model):
    name8=models.CharField(max_length=250)
    img=models.ImageField(upload_to='pics')
    desc=models.TextField()
    
    
    def __str__(self):
        return self.name8


