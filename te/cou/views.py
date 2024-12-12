from django.shortcuts import render
from .models import *

# Create your views here.
def courselist(request):
    co = course.objects.all()
    return render(request, 'listco.html', {'corse': co})

def ser_co(request):
    se = request.GET.get('id', '')
    cou = course.objects.filter(id=se)
    return render(request, 'ser.html',{'course': cou})