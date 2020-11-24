from django.db import models

# Create your models here.
class project(models.Model):
    title=models.CharField(max_length=50)
    description=models.CharField(max_length=250)
    image=models.ImageField(upload_to='port/images')
    url=models.URLField(blank=True)

