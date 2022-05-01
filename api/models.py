from pyexpat import model
from unicodedata import category
from django.db import models

# Create your models here.


class Category(models.Model):
    title = models.CharField(max_length=100)
    short_description = models.TextField(max_length=500)
    date_created = models.DateField()

    def __str__(self):
        return self.title


class Lectures(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    date_created = models.DateField()
    link = models.URLField()
    duration = models.CharField(max_length=50)

    def __str__(self):
        return self.title
