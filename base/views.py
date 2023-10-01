from django.shortcuts import render, redirect
from .models import Journey, Chapter
from .forms import JourneyForm
# Create your views here.

def index(request):

    q = request.GET.get('q') if request.GET.get('q') != None else ''
    journeys = Journey.objects.filter(name__icontains=q)
    context = {'journeys': journeys}
    return render(request, 'index.html', context)

def journey(request, pk):
    print(pk,"****************************")
    journey = Journey.objects.get(id=pk)
    chapter = Chapter.objects.filter(journey=journey)
    print(journey)
    print(chapter)
    context = {'journey': journey, 'chapters':chapter}
    return render(request, 'Journey.html', context)

def all_journeys(request):
    journeys = Journey.objects.all()
    context = {'journeys': journeys}
    return render(request, 'allJourneys.html', context)

def createJourney(request):
    form = JourneyForm()
    if request.method == 'POST':
        form = JourneyForm(request.POST)
        if form.is_valid:
            form.save()
    print("**** ",form)
    context = {'form' : form}
    
    return render(request, 'createJourney.html', context)

def updateJourney(request,pk):
    journey = Journey.objects.get(id=pk)
    form = JourneyForm(instance=journey)

    if request.method == 'POST':
        form = JourneyForm(request.POST, instance=journey)
        if form.is_valid:
            form.save()
            return redirect('index')
    context = {'form' : form}
    
    return render(request, 'updateJourney.html', context)


def deleteJourney(request,pk):
    journey = Journey.objects.get(id=pk)
    # form = JourneyForm(instance=journey)

    if request.method == 'POST':
       
        journey.delete()
        return redirect('index')
    context = {'journey' : journey}
    
    return render(request, 'deleteJourney.html', context)