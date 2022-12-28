from django.db import models
from datetime import date
# Create your models here.

class Todo(models.Model):
    title = models.CharField(max_length=200, null=False, blank=False)
    description = models.TextField(blank=True, null=True)
    date= models.DateField(default=date.today)
    estimated_end = models.DateField(null=True, blank=True)
    priority = models.IntegerField(default=3)
    