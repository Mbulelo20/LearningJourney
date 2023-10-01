from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('journey/<str:pk>', views.journey, name='journey'),
    path('all/', views.all_journeys, name='all_journeys'),
    path('startJourney', views.createJourney, name='startJourney'),
    path('updateJourney/<str:pk>', views.updateJourney, name='updateJourney'),
    path('deleteJourney/<str:pk>', views.deleteJourney, name='deleteJourney'),
]