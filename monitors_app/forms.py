from django.forms import ModelForm
from main.models import *
from django import forms

class add_schedule(ModelForm):
    class Meta:
        model = Timetable
        fields = '__all__'
        exclude = ["classroom","year_study","posted_by"]
        widgets={
            "p1":forms.Select(attrs={"class":"form-control"}),
            "p2":forms.Select(attrs={"class":"form-control"}),
            "p3":forms.Select(attrs={"class":"form-control"}),
            "p4":forms.Select(attrs={"class":"form-control"}),
            "p5":forms.Select(attrs={"class":"form-control"}),
            "p5":forms.Select(attrs={"class":"form-control"}),
            "p6":forms.Select(attrs={"class":"form-control"}),
            "day":forms.Select(attrs={"class":"form-control"}),
            "lunch_break":forms.TextInput(attrs={"class":"form-control"})

        }
    def save(self, commit=True, year_study=None,posted_by = None,classroom = None):
        instance = super().save(commit=False)
        instance.year_study = year_study
        instance.posted_by = posted_by
        instance.classroom = classroom

        if commit:
            instance.save()
        return instance
class edit_schedule(ModelForm):
    class Meta:
        model = Timetable
        fields = '__all__'
        exclude = ["classroom","year_study","posted_by","day"]
        widgets={
            "p1":forms.Select(attrs={"class":"form-control"}),
            "p2":forms.Select(attrs={"class":"form-control"}),
            "p3":forms.Select(attrs={"class":"form-control"}),
            "p4":forms.Select(attrs={"class":"form-control"}),
            "p5":forms.Select(attrs={"class":"form-control"}),
            "p5":forms.Select(attrs={"class":"form-control"}),
            "p6":forms.Select(attrs={"class":"form-control"}),

            "lunch_break":forms.TextInput(attrs={"class":"form-control"})

        }
    def save(self, commit=True, year_study=None,posted_by = None,classroom = None,day = None):
        instance = super().save(commit=False)
        instance.year_study = year_study
        instance.posted_by = posted_by
        instance.classroom = classroom
        instance.day = None
        if commit:
            instance.save()
        return instance
