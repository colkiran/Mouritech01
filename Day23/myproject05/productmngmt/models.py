from django.db import models

# Create your models here.
class Products(models.Model):
    prodname = models.CharField(max_length=100)
    manufacturer = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    price = models.FloatField()

    # def __str__(self):
    #     return self.prodname

