from django.forms import ModelForm

from .models import Journey

class JourneyForm(ModelForm):
    class Meta:
        model = Journey
        fields = '__all__'

