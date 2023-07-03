from django.forms import ModelForm
from main.models import *

class add_schedule(ModelForm):
    class Meta:
        model = Timetable
        fields = '__all__'
        exclude = ["classroom","year_study","posted_by"]
    def save(self, commit=True, year_study=None,posted_by = None,classroom = None):
        instance = super().save(commit=False)
        instance.year_study = year_study
        instance.posted_by = posted_by
        instance.classroom = classroom

        if commit:
            instance.save()
        return instance