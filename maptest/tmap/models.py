from django.db import models

# Create your models here.


class Address(models.Model):
    country = models.CharField(max_length=100, blank=True,null=True)
    state = models.CharField(max_length=100, blank=True,null=True)
    city = models.CharField(max_length=100, blank=True,null=True)
    pincode = models.CharField(max_length=100, blank=True,null=True)
    latitiude = models.CharField(max_length=100, blank=True,null=True)
    longitude = models.CharField(max_length=100, blank=True,null=True)
    address1 = models.CharField(max_length=100, blank=True,null=True)
    address2 = models.CharField(max_length=100, blank=True,null=True)
