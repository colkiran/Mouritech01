from django.db import models

# Create your models here.

class Category(models.Model):
    Categoryid = models.CharField(max_length=10, primary_key=True)
    Categoryname = models.CharField(max_length=50)


class Product(models.Model):
    Prodid = models.CharField(max_length=7, unique=True)
    Prodname = models.CharField(max_length=50)
    Categoryid = models.ForeignKey(Category, on_delete=models.CASCADE)
    Prodtype = models.CharField(max_length=30)
    Price = models.IntegerField()

