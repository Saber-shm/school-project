from django.shortcuts import render,redirect
from django.contrib import messages
from main.models import *
from .forms import *

# Create your views here.
def base(request):
    if request.user.is_authenticated:
        monitor_info = Monitor.objects.get(user = request.user)
        return render(request,"base_monitor.html",{"user_info":monitor_info})
def home_page(request):
    if request.user.is_authenticated:
        monitor_info = Monitor.objects.get(user = request.user)
        return render(request,"monitor_home.html",{"monitor_info":monitor_info,"user_info":monitor_info})
    else:
        return redirect("logins")

def add_schedule_ed_level(request):
    if request.user.is_authenticated:
        monitor_info = Monitor.objects.get(user = request.user)
        ed_data = Education_level.objects.all()

        return render(request,"add_schedule_ed_level.html",{"ed_data":ed_data,"user_info":monitor_info})
    else:
        return redirect("logins")
def add_schedule_level(request,ed_level):
    if request.user.is_authenticated:
        monitor_info = Monitor.objects.get(user = request.user)
        levls = Level.objects.filter(year_study = monitor_info.year_study,education_level = ed_level)
        print(levls)
        return render(request,"add_schedule_level.html",{"levels":levls,"user_info":monitor_info})
    else:
        return redirect("logins")
def add_schedule_classroom(request,level):
    if request.user.is_authenticated:
        monitor_info = Monitor.objects.get(user = request.user)
        levelr = Level.objects.get(pk=level)
        print(levelr)
        classrooms = Classroom.objects.filter(level = levelr)
        print(classrooms)
        return render(request,"add_schedule_classroom.html",{"classrooms":classrooms,"user_info":monitor_info})
    else:
        return redirect('logins')
def add_schedule_form(request,classroom):
    if request.user.is_authenticated:
        monitor_info = Monitor.objects.get(user = request.user)
        classroom =  Classroom.objects.get(pk = classroom)
        scheduler = Timetable.objects.filter(classroom = classroom,year_study = classroom.year_of_study)
        if request.method == "POST":
            form = add_schedule(request.POST)
            
            if form.is_valid():
                day_check = form.cleaned_data["day"]
                schedule = form.save(commit=False)
                schedule.year_study = monitor_info.year_study
                schedule.posted_by = request.user
                schedule.classroom = classroom
                if scheduler.exists() and Timetable.objects.filter(day = day_check):
                    messages.success(request,"day already in database")
                    return render(request,'add_schedule_form.html',{"form":form,"message":messages.get_messages(request),"user_info":monitor_info})
                else:
                    schedule.save()
                    return redirect("add_schedule_classroom",level = classroom.level.id)
        else:
            form = add_schedule
        return render(request,"add_schedule_form.html",{"form":form,"user_info":monitor_info})
def schedules_posted_classroom(request):
    if request.user.is_authenticated:
        monitor_info = Monitor.objects.get(user = request.user)
        datas = Timetable.objects.filter(posted_by = request.user)
        classes = []
        for i in datas:
            if i.classroom not in classes:
                classes.append(i.classroom)
        print(classes)
        return render(request,"schedules_posted_classroom.html",{"schedules":classes,"user_info":monitor_info})
    else:
        return redirect('logins')
    
def schedules_posted_days(request,classroom):
    if request.user.is_authenticated:
        monitor_info = Monitor.objects.get(user = request.user)
        datas = Timetable.objects.filter(classroom = classroom )
        print(datas)
        return render(request,'schedules_posted_days.html',{"data":datas,"user_info":monitor_info})
    else:
        return redirect("logins")
def schedule_posted_form(request,form_id):
    if request.user.is_authenticated:
        monitor_info = Monitor.objects.get(user = request.user)
        schedule1 = Timetable.objects.get(pk = form_id)
        classe = schedule1.classroom
        day = schedule1.day
        
        form = edit_schedule(request.POST or None, instance=schedule1)
        if form.is_valid():
            schedule = form.save(commit=False)
            schedule.year_study = monitor_info.year_study
            schedule.posted_by = request.user
            schedule.classroom = classe
            schedule.day = day
            schedule.save()
            return redirect("monitors_home_page")
        return render(request,"schedules_posted_form.html",{"data":schedule1,"form":form,"message":messages.get_messages(request),"user_info":monitor_info})