from django.db import models

# Create your models here.
class course(models.Model):
    id = models.CharField(primary_key=True, max_length=25)
    na = models.CharField(max_length=25)
    tna = models.CharField(max_length=25)
