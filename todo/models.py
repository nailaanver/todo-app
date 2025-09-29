from django.db import models
from django.utils import timezone


# Create your models here.
class Tables(models.Model):
    task = models.CharField(max_length=255)
    status = models.CharField(max_length=255)
    actions = models.CharField(max_length=255)
    created_date = models.DateField(auto_now_add=True)
    due_date = models.DateField(null=True,blank=True)
    def __str__(self):
        return self.task
    
    