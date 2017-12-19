from __future__ import unicode_literals
from django.db import models

class Dojo(models.Model):
    name = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=2)
    desc = models.TextField()

class Ninjas(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    dojo = models.ForeignKey(Dojo, related_name="ninjas") #ninjas is used for ? 

# my_book = Book.objects.create(first_name="Bob", last_name="Bobbers", dojo= Dojo.objects.get(id=2))


# ## foreign key assignment 
# my_book = Book.objects.create(title="Little Women", author=Author.objects.get(id=2))


# ####Adding a relationship between two existing records: #####
# this_book = Book.objects.get(id=4)
# this_publisher = Publisher.objects.get(id=2)
# this_publisher.books.add(this_book)


