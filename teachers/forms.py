from django import forms
from main.models import *
class add_lesson_forms(forms.ModelForm):
    class Meta:
        model = Lesson
        fields = "__all__"
        exclude = ['teacher',"classroom","module"]
        widgets={
            "title":forms.TextInput(attrs={"class":"form-control"}),
            "file":forms.FileInput(attrs={'class': 'form-control'}),
            "year_study":forms.Select(attrs={"class":"form-control"})

        }
    def save(self, commit=True, teacher=None,module = None,classroom = None):
        instance = super().save(commit=False)
        instance.teacher = teacher
        instance.module = module
        instance.classroom = classroom

        if commit:
            instance.save()
        return instance

class add_grade_forms(forms.ModelForm):
    class Meta:
        model = Grade
        fields = "__all__"
        exclude = ["teacher","classroom_grade","student","module"]
        widgets={
            "module":forms.Select(attrs={"class":"form-control"}),
            "note":forms.NumberInput(attrs={'class': 'form-control'}),
            "exam":forms.Select(attrs={"class":"form-control"})

        }
    def save(self,commit = True,teacher = None,classroom_grade = None,student = None,module = None):
        instance = super().save(commit = False)
        instance.teacher = teacher
        instance.classroom_grade = classroom_grade
        instance.student = student
        instance.module = module


        if commit:
            instance.save()
        return instance 
class add_devoir_forms(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['deadline'].widget = forms.widgets.DateInput(
            attrs={
                'type': 'date', 'placeholder': 'yyyy-mm-dd (DOB)',
                'class': 'form-control'
                }
            )
    class Meta:
        model = Homework
        fields = "__all__"
        exclude = ["teacher","classroom","year_study"]
        widgets={
            "title":forms.TextInput({"class":"form-control"}),
            "descriptions":forms.Textarea({"class":"form-control"}),
            "module":forms.Select({"class":"form-control"})

        }
    def save(self,commit = True,teacher = None,classroom = None,year_study = None):
        instance = super().save(commit = False)
        instance.teacher = teacher
        instance.classroom = classroom
        instance.year_study = year_study

        if commit:
            instance.save()
        return instance 