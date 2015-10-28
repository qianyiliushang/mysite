# coding:utf-8
from django.db import models
import sys

reload(sys)
sys.setdefaultencoding('utf-8')


# Create your models here.
class SignUp(models.Model):
    def __str__(self):
        return self.full_name

    email = models.EmailField()
    full_name = models.CharField(max_length=120, blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)
