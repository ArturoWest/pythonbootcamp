from django.db import models

# Create your models here.

class Math(models.Model):
    operations = models.CharField(max_length=10)
    arg_a = models.IntegerField()
    arg_b = models.IntegerField()

#def __str__(self):
