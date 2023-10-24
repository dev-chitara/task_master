from django.db import models

# Create your models here.
class Users(models.Model):
    user_name = models.CharField(max_length=20)
    role_title = models.CharField(max_length=20)
    department = models.CharField(max_length=20)
    location = models.FloatField()
    emp_no = models.IntegerField()

