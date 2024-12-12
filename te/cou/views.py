from django.shortcuts import render
from .models import *

# Create your views here.
def courselist(request):
    co = course.objects.all()
    return render(request, 'listco', {'corse': co})
