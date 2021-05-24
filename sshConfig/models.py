from django.db import models


# Create your models here.
class ssh_gourp(models.Model):
    group_name = models.CharField(max_length=20)
    email_name = models.CharField(max_length=20)


class ssh_user(models.Model):
    username = models.CharField(max_length=20)
    userpaaword = models.CharField(max_length=100)
    ipaddress = models.CharField(max_length=20)
    group_id = models.SmallIntegerField(default=0)
