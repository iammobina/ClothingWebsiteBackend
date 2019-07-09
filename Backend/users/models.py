from django.db import models
#from phone_field import PhoneField
from django.contrib.auth.models import User

class Design(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    Title = models.CharField(max_length=100)
    Description = models.TextField(max_length=300, blank=True)
    Image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.Title

class User(models.Model):
    #User = models.OneToOneField(User,on_delete=models.CASCADE)
    Photo = models.ImageField(upload_to='userimage/', blank=True)
    Name = models.CharField(max_length=100, blank=False)
    Lastname = models.CharField(max_length=100,blank=False)
    userId = models.CharField(max_length=100,blank=False)
    Password = models.CharField(max_length=100, blank=False)
    Confirm = models.CharField(max_length=100, blank=False, help_text= 'Confirm your password')
    Phone = models.CharField(max_length=15, blank=True)
    Email = models.EmailField(max_length=100, blank=True)
    Address = models.TextField(max_length=300, blank=True)

    def __str__(self):
        return self.userId