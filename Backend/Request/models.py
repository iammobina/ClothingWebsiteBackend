from django.db import models


class Tailor(models.Model):
    username = models.CharField(max_length=30, blank=False, null=False)
    password = models.CharField(max_length=20, blank=False, null=False)


class User(models.Model):
    username = models.CharField(max_length=30, blank=False, null=False)
    password = models.CharField(max_length=20, blank=False, null=False)


class Request(models.Model):
    design = models.ImageField(blank=False, null=False, upload_to='requests/', )
    phoneNumber = models.IntegerField(default= 1,)
    description = models.CharField(default='description', max_length=1000)
    tailor = models.ForeignKey(to=Tailor, related_name='receiver', on_delete=models.CASCADE)
    user = models.ForeignKey(to=User, related_name='sender',on_delete=models.CASCADE)
    isDone = models.BooleanField(default= False,)

