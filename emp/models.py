from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class employee(models.Model):
    User = models.ForeignKey(User,on_delete=models.CASCADE)
    age = models.IntegerField()
    gender = models.CharField(max_length=10)
    email = models.EmailField(verbose_name='email address', max_length=260, unique=True)
    department = models.CharField(max_length=260)
    company_name = models.CharField(max_length=260)
    leave_availabel = models.IntegerField()



class emp_leave(models.Model):
    date = models.DateTimeField()
    reason = models.CharField(max_length=1000)
    name = models.CharField(max_length=260)


class holiday(models.Model):
    date = models.DateTimeField()
    name = models.CharField(max_length=260)
