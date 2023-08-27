from django.shortcuts import render
from .models import Journey, Chapter
# Create your views here.

def index(request):
    journeys = Journey.objects.all()
    context = {'journeys': journeys}
    return render(request, 'index.html', context)

def journey(request, pk):
 
    journey = Journey.objects.get(id=pk)
    chapter = Chapter.objects.all()

    context = {'journey': journey, 'chapters':chapter}
    print()
    return render(request, 'Journey.html', context)