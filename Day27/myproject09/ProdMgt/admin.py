from django.contrib import admin
from .models import Category, Product

# Register your models here.
@admin.register(Product, Category)
class ProdAdmin(admin.ModelAdmin):
    pass

