from django.shortcuts import render
from .models import Journey
# Create your views here.

def index(request):
    journeys = Journey.objects.all()
    context = {'journeys': journeys}
    return render(request, 'index.html', context)