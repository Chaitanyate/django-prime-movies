from django.db import models

class blog(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    date=models.DateField()