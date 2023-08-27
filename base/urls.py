from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('journey/<str:pk>', views.journey, name='journey'),
]