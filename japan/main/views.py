from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index (request):
    data = {
        'title': 'Home page',
        'values': ['Some', 'Hello', '123'],
    }

    return render(request, 'main/index.html', data)

def about (request):
    return render(request, 'main/about.html')