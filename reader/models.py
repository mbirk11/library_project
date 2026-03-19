from django.db import models
from book.models import Book

class Reader(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20, null=True, blank=True)
    age = models.IntegerField(null=True, blank=True)
    password = models.CharField(max_length=128, default='123')
    books = models.ManyToManyField(Book, related_name='readers')

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
