from django.db import models

# Create your models here.


class register(models.Model):
    name = models.CharField(max_length=20)
    password = models.CharField(max_length=100)
    mail = models.CharField(max_length=100)
