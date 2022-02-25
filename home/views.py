from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from .models import Opening, Food


# Create your views here.
def index(request):
    ''' A view to return the index page '''

    return render(request, 'home/index.html')

def opening_times(request):
    ''' A view to return the opening times '''
    opening = Opening.objects.all()
    food = Food.objects.all()

    template = 'home/opening_times.html'
    context = {
        'opening': opening,
        'food': food,
    }

    return render(request, template, context)
