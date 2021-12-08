from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Status(models.Model):
    title = models.CharField(max_length=200, null=False)


class Record(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, null=False)
    phone = models.CharField(max_length=200, null=False)
    description = models.CharField(max_length=200)
    status_id = models.ForeignKey(Status, null=True, on_delete= models.CASCADE)
    user_id = models.OneToOneField(User, null=False, on_delete=models.CASCADE)
