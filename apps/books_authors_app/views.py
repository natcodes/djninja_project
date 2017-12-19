from __future__ import unicode_literals
from django.shortcuts import render, HttpResponse, redirect
def index(request):
    return render(request, "books_authors_app/index.html")

# Create your views here.
