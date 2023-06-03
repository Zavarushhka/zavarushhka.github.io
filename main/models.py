from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Order(models.Model):
    name = models.CharField("Name", max_length=20)
    email = models.EmailField("Email", max_length=50 )
    phone = models.CharField("Phone", max_length=20)

    def __str__(self):
        data = self.name + ' ' + self.phone
        return data
    
    class Meta:
        verbose_name = "Name"
