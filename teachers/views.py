from django.shortcuts import render,redirect
from django.contrib import messages
from .forms import *
# Create your views here.
"""def base_teacher(request):
    if request.user.is_authenticated:
        """
def home_page_teacher(request):
    if request.user.is_authenticated:
        teacher_info = Teacher.objects.get(user = request.user)
        return render(request,"home_page_teacher.html",{"user_info":teacher_info})

    else:
        return redirect("logins")
def add_lesson(request):
    if request.user.is_authenticated:
        teacher_info = Teacher.objects.get(id = request.user.id)
        return render(request,"add_lesson.html",{'teacher':teacher_info,"user_info":teacher_info})


def add_lesson_module(request,classroom):

    if request.user.is_authenticated:
        classroom2 = classroom.split()
        classroom3 = classroom2[-1]
        classroom_r = Classroom.objects.get(name = classroom3)
        print(classroom_r)

        teacher_info = Teacher.objects.get(user = request.user)
        classroom2 = classroom.split()
        classroom3 = classroom2[-1]
        classroom_r = Classroom.objects.get(name = classroom3)
        if request.method == 'POST':
            form = add_lesson_forms(request.POST, request.FILES)

            if form.is_valid():
                lesson = form.save(commit=False)
                lesson.teacher = teacher_info
                lesson.module = teacher_info.module
                lesson.classroom = classroom_r
                lesson.year_study = teacher_info.year_study.id
                lesson.save()
                return redirect('teacher_home_page')
        else:
            form = add_lesson_forms()
        return render(request, "add_lesson_module.html", {'form': form,"user_info":teacher_info})
    else:
        return redirect("logins")

def students_classroom(request):
    if request.user.is_authenticated:
        teacher_info = Teacher.objects.get(user = request.user)
        classrooms = teacher_info.classroom
        print(classrooms)
        return render(request,'classrooms_students.html',{"classrooms":classrooms,"user_info":teacher_info})
    else:

        return redirect('logins')

def students_list(request,classroom):
    if request.user.is_authenticated:
        teacher_info = Teacher.objects.get(user = request.user)
        students = Student.objects.filter(classroom = classroom)
        classr = Classroom.objects.get(pk = classroom)
        return render(request,'students_list.html',{"students":students,"classroom":classr,"user_info":teacher_info})
    else:
        return redirect("logins")

def Student_info(request,student):
    if request.user.is_authenticated:
        student_info = Student.objects.get(pk = student)
        teacher_info = Teacher.objects.get(user = request.user)
        return render(request,"student_info.html",{"student_info":student_info,"user_info":teacher_info})

def search_for_student_form(request,classroom):
    if request.user.is_authenticated:
        teacher_info = Teacher.objects.get(user = request.user)
        if request.method == "POST":
            first_name = request.POST.get("first_name")
            last_name = request.POST.get("last_name")
            print(first_name,last_name)
            year_study = teacher_info.year_study
            return redirect("student_result_query",first_name = first_name,last_name = last_name)
        return render(request,'search_for_student_form.html',{"user_info":teacher_info})
def student_search_result(request,first_name,last_name):
    if request.user.is_authenticated:  
        print(first_name)
        print(last_name)
        teacher_info = Teacher.objects.get(user = request.user)
        students = Student.objects.filter(first_name = first_name,last_name = last_name,year_study= teacher_info.year_study)
        return render(request,"student_result_search.html",{"students":students,"user_info":teacher_info})
def add_grade(request):
    if request.user.is_authenticated:
        teacher_info = Teacher.objects.get(user = request.user)

        return render(request,"add_grade_list.html",{"teacher_info":teacher_info,"user_info":teacher_info})

    else:
        return redirect("logins")
def add_grade_classroom_year(request,classroom):
    if request.user.is_authenticated:
        teacher_info = Teacher.objects.get(user = request.user)
        year_of_study = Year_study.objects.all()
        return render(request,"add_grade_year.html",{"years":year_of_study,"classroom": classroom,"user_info":teacher_info})


def add_grade_classroom(request,classroom):
    if request.user.is_authenticated:
        teacher_info = Teacher.objects.get(user = request.user)
        year_of_study = Year_study.objects.get(pk = teacher_info.year_study.id)
        classroomr = Classroom.objects.get(pk = classroom)
        classroom_grade_info = Classroom_grade.objects.filter(classroom = classroomr,year_study = year_of_study)
        return render(request,'add_grade_classroom.html',{"class_data":classroom_grade_info,"user_info":teacher_info,"classroom":classroom,"year_":str(year_of_study)})
    else:
        return redirect("logins")
def add_grade_student(request,classroom_grade1,classroom):
    if request.user.is_authenticated:
        teacher_info = Teacher.objects.get(user = request.user)
        print(classroom)
        classroom_ = Classroom.objects.get(pk = classroom)
        students = Student.objects.filter(classroom = classroom_)
        print(students)
        return render(request,"add_grade_student.html",{"students":students,"user_info":teacher_info,"class_grade":classroom_grade1})

def add_grade_form(request,classroom_grade,student1):
    if request.user.is_authenticated:
        teacher_info = Teacher.objects.get(user = request.user)
        student = Student.objects.get(pk =student1)
        class_grade = Classroom_grade.objects.get(pk = classroom_grade)
        grades = Grade.objects.filter(student = student)

        
        if request.method == "POST":
            form = add_grade_forms(request.POST)
            if form.is_valid():
                student_check = student
                module_check = teacher_info.module
                classroom_grade_check = class_grade
                exam_check  = form.cleaned_data["exam"]
                if grades.exists() and Grade.objects.filter(classroom_grade = class_grade) and Grade.objects.filter(module = module_check) and Grade.objects.filter(exam = exam_check):
                    messages.success(request,"Grade already in database")
                    return render(request, "add_grade1.html",{"class":class_grade,"user_info":teacher_info,"form":form,"message":messages.get_messages(request)})

                else:
                    print(student_check,module_check,classroom_grade_check)
                    grade = form.save(commit=False)
                    grade.teacher = teacher_info
                    grade.student = student
                    grade.classroom_grade = class_grade
                    grade.module = teacher_info.module
                    grade.save()
                    return redirect("teacher_home_page")
        else:
            form = add_grade_forms
        return render(request, "add_grade1.html",{"class":class_grade,"user_info":teacher_info,"form":form,"message":messages.get_messages(request)})


def add_devoir(request):
    if request.user.is_authenticated:
        teacher_info = Teacher.objects.get(user = request.user)
        classrooms = teacher_info.classroom
        return render(request,"devoirpage1.html",{"classrooms":classrooms,"user_info":teacher_info})
def add_devoir_form(request,classroom):
    if request.user.is_authenticated:
        teacher_info = Teacher.objects.get(user = request.user)
        classroom = Classroom.objects.get(pk = classroom)
        if request.method == "POST":
            form = add_devoir_forms(request.POST,request.FILES)

            if form.is_valid():

                grade = form.save(commit=False)
                grade.teacher = teacher_info
                grade.classroom = classroom
                grade.year_study = teacher_info.year_study
                grade.save()
                return redirect('teacher_home_page')
            
        else:
            form = add_devoir_forms
        return render(request,"add_devoir_form.html",{"form":form,"user_info":teacher_info})
def lessons_posted(request):
    if request.user.is_authenticated:
        teacher_info = Teacher.objects.get(user = request.user)
        lessons = Lesson.objects.filter(teacher = teacher_info)
        print(lessons)
        return render(request,"lessons_posted.html",{"lessons":lessons,"user_info":teacher_info})
def lesson_update_form(request,lesson_id):
    if request.user.is_authenticated:
        teacher_info = Teacher.objects.get(user = request.user)
        lesson = Lesson.objects.get(pk = lesson_id)
        form = add_lesson_forms(request.POST or None,request.FILES or None,instance=lesson)
        print(lesson.classroom.id)
        classroomr = Classroom.objects.get(pk = lesson.classroom.id)
        print(lesson.classroom)
        if form.is_valid():
            lesson = form.save(commit=False)
            lesson.teacher = teacher_info
            lesson.module = teacher_info.module
            lesson.classroom = classroomr
            lesson.save()
            return redirect("teacher_home_page")
        
        return render(request,"lesson_update_form.html",{"form":form,"user_info":teacher_info})
def grade_posted(request):
    if request.user.is_authenticated:
        teacher_info = Teacher.objects.get(user = request.user)
        grades_posted_by_teacher = Grade.objects.filter(teacher = teacher_info)
        print(grades_posted_by_teacher)
        return render(request,"grade_posted.html",{"grades":grades_posted_by_teacher})
def grade_update_form(request,grade_id):
    if request.user.is_authenticated:
        grade = Grade.objects.get(pk = grade_id)
        classroom = grade.classroom_grade
        student = grade.student

        teacher_info =  Teacher.objects.get(user = request.user)


        form = add_grade_forms(request.POST or None,instance = grade)
        if form.is_valid():
            grade = form.save(commit=False)
            grade.teacher = teacher_info
            grade.student = student
            grade.classroom_grade = classroom
            grade.year_study = teacher_info.year_study
            grade.module = teacher_info.module
            grade.save()
            return redirect('teacher_home_page')        
        return render(request,'grade_update_form.html',{"form":form,"user_info":teacher_info})

def add_exam_alert_classroom(request):
    if request.user.is_authenticated:
        teacher_info = Teacher.objects.get(user = request.user)
        return render(request,"add_exam_alert.html",{"user_info":teacher_info})
    else:
        return redirect("logins")
    
def add_exam_alert_form_view(request,classroom):
    if request.user.is_authenticated:
        teacher_info = Teacher.objects.get(user = request.user)
        if request.method == "POST":
            form = add_exam_alert_form(request.POST)
            if form.is_valid():
                instance = form.save(commit=False)
                instance.posted_by = request.user
                instance.module = teacher_info.module
                instance.year_study = teacher_info.year_study
                instance.classroom = Classroom.objects.get(pk = classroom)
                instance.save()
                return redirect("teacher_home_page")
        else:
            form = add_exam_alert_form
        return render(request,'add_exam_alert_form.html',{"form":form})
    else:
        return redirect("logins")
def exam_alerts_posted(request):
    if request.user.is_authenticated:
        teacher_info = Teacher.objects.get(user = request.user)
        data = Exam_alert.objects.filter(posted_by = request.user)
        return render(request,'exam_alerts_posted.html',{"data":data})
    else:
        return redirect("logins")
def edit_exam_alert_form(request,id_form1):
    if request.user.is_authenticated:
        teacher_info = Teacher.objects.get(user = request.user)
        d = Exam_alert.objects.get(pk = id_form1)
        form = add_exam_alert_form(request.POST or None,instance=d)
        print(d.classroom)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.posted_by = request.user
            instance.module = teacher_info.module
            instance.year_study = teacher_info.year_study
            instance.classroom = Classroom.objects.get(pk = d.classroom.id)
            instance.save()
            return redirect("teacher_home_page")
        return render(request,"edit_exam_alert.html",{"form": form})
    else:
        return redirect("login")
"""def add_exam_alert_form(request,classroom):
    if request.user.is_authenticated:
        teacher_info = Teacher.objects.get(user = request.user)
        """
    

"""     else:
if request.user.is_authenticated:
        teacher_info = Teacher.objects.get(user = request.user)
        if request.method == 'POST':
            form = add_grade_forms(request.POST)
            if form.is_valid():
                grade = form.save(commit=False)
                grade.teacher = request.user
                grade.save()
        else:
            form = add_grade_forms

        return render(request,"add_grade1.html",{"form":form})
    else:
        return redirect("logins")
"""

"""def add_lesson_classroom(request,module,level):
    if request.user.is_authenticated:
        if request.method == 'POST':
            print("ç")
            form = add_lesson_forms(request.POST, request.FILES)
            print(request.user.teacher)
            print(level)
            print(module)
            if form.is_valid():
                lesson = form.save(commit=False)
                lesson.teacher = request.user.teacher
                #lesson.module = module
                lesson.save()
                return redirect('teacher_home_page')
        else:
            form = add_lesson_forms()
        return render(request, "add_lesson_module.html", {'form': form})
    else:
        return redirect('logins')
"""








"""
    if request.user.is_authenticated:
        try:
            student_info = Student.objects.get(user=request.user)
            student_level = student_info.level
            data_user = Lesson.objects.filter(level = student_level)

            return render(request,"per_error.html",{"user":request.user.username,"teacher":False})

        except:
            try:
                if request.method == 'POST':
                    form = add_lesson_forms(request.POST, request.FILES)
                    if form.is_valid():
                        lesson = form.save(commit=False)
                        lesson.teacher = request.user.teacher  # Assign the Teacher instance
                        lesson.save()
                        return redirect('teacher_home_page')


                else:
                    form = add_lesson_forms()
                return render(request,"add_lesson.html",{'form': form})
            except:
                return render(request,"per_error.html",{"teacher":True ,"user":request.user.username})

    else:
        return redirect('logins')
"""