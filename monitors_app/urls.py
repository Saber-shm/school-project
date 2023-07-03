from django.urls import path
from .views import *

urlpatterns =  [
    path("home_page/",home_page,name = "monitors_home_page"),
    path("add_schedule_ed/",add_schedule_ed_level,name = "add_schedule_ed"),
    path("add_schedule_level/<ed_level>",add_schedule_level,name = "add_schedule_level"),
    path("add_schedule_class/<level>",add_schedule_classroom,name = "add_schedule_classroom"),
    path("add_schedule_form/<classroom>",add_schedule_form,name = "add_schedule_form"),
    path("schedules_posted_classroom/",schedules_posted_classroom,name = "schedules_posted_classroom"),
    path("schedules_posted_days/<classroom>",schedules_posted_days,name = "schedules_posted_days")

]