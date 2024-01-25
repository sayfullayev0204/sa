from django.db import models
from django.urls import reverse
# Create your models here.
class Category(models.Model):
    nomi = models.CharField(max_length=256, unique=True)
    malumoti = models.TextField(blank=True)
    rasmi = models.ImageField(upload_to='photoes/category', blank = True)

    def __str__(self):
        return self.nomi


from django.db import models
from .models import Category
from django.urls import reverse
# Create your models here.
class Product(models.Model):
    Turi = models.ForeignKey(Category, on_delete=models.CASCADE,  blank=True, null=True, unique=True)
    Ismingiz = models.CharField(max_length=100,  blank=True, null=True, unique=True)
    nomi=models.CharField(max_length=500,  blank=True, null=True, unique=True)
    malumoti = models.TextField(max_length=500,  blank=True, null=True, unique=True)
    narxi = models.CharField(max_length=200 , blank=True, null=True, unique=True)
    rasmi = models.ImageField(upload_to = 'photoes/products', blank=True, null=True, unique=True)
    ulanish = models.CharField(max_length=100,  blank=True, null=True, unique=True)
    def __str__(self) -> str:
        return self.nomi

