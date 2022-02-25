from django.shortcuts import render, get_object_or_404
from .models import Opening


# Create your views here.
def index(request):
    ''' A view to return the index page '''

    return render(request, 'home/index.html')

def opening_times(request):
    ''' A view to return the opening times '''
    opening = OpeningTime.objects.all()
    context = {
        'opening': opening
    }

    return render(request, 'home/opening_times.html', context)
