from django.shortcuts import render
from .models import Card

# Create your views here.

def index(request):
    dest = Card.objects.all()


    return render(request, 'index.html', {'dest':dest})