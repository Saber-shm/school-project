from django.shortcuts import render,redirect, get_object_or_404
from django.http import HttpResponse
from main.models import *
from django.apps import apps
from django.db.models import Q

# Create your views here.

def home_page(request):
    if request.user.is_authenticated:
        student_info = Student.objects.get(user = request.user)
    return render(request,"home_page.html",{"user_info":student_info})


def lessons_page(request):

    if request.user.is_authenticated:
        try:
            student_info = Student.objects.get(user=request.user)
            student_level = student_info.level
            data_user = Lesson.objects.filter(level = student_level)

            return render(request,"lessons_page.html",{"d":data_user,"user_info":student_info})

        except:
            return render(request,'error_lesson.html')
    else:
        redirect("logins")
def download_pdf(request,pdf_id):
    pdf = get_object_or_404(Lesson, pk=pdf_id)
    response = HttpResponse(pdf.file, content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="{}.pdf"'.format(pdf.title)
    return response

def error_lesson(request):
    return render(request,'error_lesson.html')


def lesson_module(request,module_name):
    if request.user.is_authenticated:
        student_info = Student.objects.get(user = request.user)
        student_level = student_info.classroom
        module_get = Module.objects.get(id = module_name)
        lessons_get = Lesson.objects.filter(classroom = student_level)
        lesson_module_get = lessons_get.filter(module = module_name)
        if request.method == "POST":
            search_i = request.POST["search"]
            data = Lesson.objects.filter(Q(title__contains = search_i),year_study = student_info.year_study,module = module_name)
            print(data)
            return redirect("lesson_search",result=data)

        return render(request,'lesson_module.html',{"lesson":lesson_module_get,"module":module_get,"user_info":student_info})
    else:
        return redirect("logins")

def lesson_page(request,lesson_title):
    if request.user.is_authenticated:
        student_info = Student.objects.get(user = request.user)

        lesson_data = Lesson.objects.filter(title = lesson_title)
        return render(request,"lesson_page.html",{"lesson_data": lesson_data,"user_info":student_info})
    else:
        return redirect("logins")
def lesson_search(request,result):
    if request.user.is_authenticated:
        student_info = Student.objects.get(user = request.user)
        return render(request,'lesson_search.html',{"result":result})
def grade_view(request,year,semestre):
    if request.user.is_authenticated:
        classgrade = Classroom_grade.objects.get(semestre = semestre)
        student_info = Student.objects.get(user = request.user)
        classroom = student_info.classroom
        modules = classroom.modules
        grades = Grade.objects.filter(classroom_grade = classgrade,student= student_info)
        year = Year_study.objects.get(pk = year)
        semestre = Semestre.objects.get(pk = semestre)
        dic_grade = {}
        print(modules.all())
        for m in modules.all():
            print(m)
            if m not in dic_grade.keys():
                dic_grade[m] = {}            
                e = grades.filter(module = m)
                for i in e:
                    if i.exam not in dic_grade[m]:
                        dic_grade[m][i.exam] = i.note

        print(dic_grade)
        return render(request,"grade_view.html",{"year":year,"semestre":semestre,"user_info":student_info,"class_grade":classgrade,"modules":modules,"f":grades,"dic_grade":dic_grade})
    else:
        return redirect("logins")
def module_page(request):
    if request.user.is_authenticated:
        student_info = Student.objects.get(user = request.user)
        modules_available = Module.objects.filter(level = student_info.level)

        return render(request,'modules.html',{"modules":modules_available,"username":request.user,"user_info":student_info})
    
def myprofile_page(request):
    if request.user.is_authenticated:
        student_info = Student.objects.get(user = request.user)
        return render(request,'myprofile_page.html',{"student_info":student_info,"user_info":student_info})
    
    else:
        return redirect("logins")

def grade_year(request):
    if request.user.is_authenticated:
        student_info = Student.objects.get(user = request.user)
        years = Year_study.objects.all()
        return render(request,"grade_year.html",{"years":years,"students_info":student_info,"user_info":student_info})
    else:
        return redirect('logins')

def grade_semetre(request):
    if request.user.is_authenticated:
        semestres = Semestre.objects.all()
        student_info = Student.objects.get(user = request.user)
        
        return render(request,'grade_semestre.html',{"semestres":semestres,"year":student_info.year_study,"user_info":student_info})
    
def devoir_list(request):
    if request.user.is_authenticated:
        student_info = Student.objects.get(user = request.user)
        classroom = student_info.classroom
        devoirs = Homework.objects.filter(classroom = classroom)
        return render(request,"devoir_list.html",{"devoirs":devoirs,"user_info":student_info})
    else:
        return redirect("logins")
def devoir_view(request,devoir_id):
    if request.user.is_authenticated:
        student_info = Student.objects.get(user = request.user)
        devoir = Homework.objects.get(pk = devoir_id)
        return render(request,'devoir_view.html',{"devoir":devoir,"user_info":student_info})
    
def timetable_view(request):
    if request.user.is_authenticated:
        student_info = Student.objects.get(user = request.user)
        classroom = student_info.classroom
        timetable_data = Timetable.objects.filter(classroom = classroom,year_study = student_info.year_study)
        return render(request,'timetable_view.html',{"data":timetable_data,"classroom":classroom,"user_info":student_info})
    else:
        return redirect("logins")
def alert_exam_list(request):
    if request.user.is_authenticated:
        student_info = Student.objects.get(user = request.user)
        data = Exam_alert.objects.filter(year_study= student_info.year_study, classroom = student_info.classroom)
        print(data)
        print()
        return render(request,'alert_exam_list.html',{"data":data,"classroom":student_info.classroom})
    else:
        return redirect("logins")
def alert_exam_view(request,exam_id):
    if request.user.is_authenticated:
        student_info = Student.objects.get(user = request.user)
        data = Exam_alert.objects.get(pk = exam_id)
        return render(request,'exam_alert_view.html',{"data":data,"user_info":student_info})
    else:
        return redirect("logins")