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
