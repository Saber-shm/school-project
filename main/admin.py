from django.contrib import admin
from .models import *
import inspect
import sys


admin.site.register(messages_contact)
admin.site.register(Student)
admin.site.register(Level)
admin.site.register(Teacher)
admin.site.register(Lesson)
admin.site.register(Grade)
admin.site.register(Classroom)
admin.site.register(Module)
admin.site.register(Year_study)
admin.site.register(Education_level)
admin.site.register(Attendence_report)
admin.site.register(Classroom_grade)
admin.site.register(Semestre)
admin.site.register(Homework)
admin.site.register(Timetable)
admin.site.register(Monitor)
admin.site.register(Exam_alert)