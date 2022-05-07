from django.shortcuts import render
from .models import Pizza

# Create your views here.

def index(request):
    return render(request, 'MainApp/index.html')


def pizza(request):
    pizza = Pizza.objects.all()

    context = {'pizza': pizza}

    return render(request,'MainApp/pizza.html', context)