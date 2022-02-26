from audioop import ratecv
from pydoc import describe
from statistics import mode
from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=70)
    rating = models.IntegerField()
    year = models.IntegerField()
    is_best_selling = models.BooleanField()
    author = models.CharField(max_length=100, null=True)
    
    def __str__(self):
        return f"{self.title} - {self.rating} - {self.year}"