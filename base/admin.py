from django.contrib import admin
from django import forms

# Register your models here.
from .models import Journey
from .models import Chapter


class JourneyAdminForm(forms.ModelForm):
    class Meta:
        model = Journey
        fields = '__all__'  # Include all fields from the model
        widgets = {
            'start_date': forms.DateInput(attrs={'type': 'date'}),
            'end_date': forms.DateInput(attrs={'type': 'date'}),
        }

class JourneyAdmin(admin.ModelAdmin):
    form = JourneyAdminForm
    list_display = ('name', 'start_date', 'end_date', 'updated', 'created')


class ChapterAdmin(admin.ModelAdmin):
    list_display = ('title',)
    # Other fields you want to display in the list view

    def body_formatted(self, obj):
        return obj.body.replace('\n', '--------------------------------------')  # Convert line breaks to HTML line breaks

    body_formatted.allow_tags = True
    body_formatted.short_description = 'Body'


admin.site.register(Journey, JourneyAdmin)
admin.site.register(Chapter, ChapterAdmin)

