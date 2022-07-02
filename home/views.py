from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

# Create your views here.
def home(request):
    date = datetime.now()
    date.strftime("%b %d, %Y, %H:%M:%S")
    return render(request, 'home/home.html', {'today': date})
