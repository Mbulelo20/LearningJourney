from django.contrib import admin
from django import forms

# Register your models here.
# from .models import Journey


# class JourneyAdminForm(forms.ModelForm):
#     class Meta:
#         model = Journey
#         fields = '__all__'  # Include all fields from the model
#         widgets = {
#             'start_date': forms.DateInput(attrs={'type': 'date'}),
#             'end_date': forms.DateInput(attrs={'type': 'date'}),
#         }

# class JourneyAdmin(admin.ModelAdmin):
#     form = JourneyAdminForm
#     list_display = ('name', 'start_date', 'end_date', 'updated', 'created')
    # Other customizations as needed

# admin.site.register(Journey)

