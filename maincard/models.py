from django.db import models

# Create your models here.

class Card(models.Model):
    image = models.ImageField(upload_to= 'picture')
    name = models.CharField(max_length=20)
    price = models.IntegerField()
    description = models.TextField()


