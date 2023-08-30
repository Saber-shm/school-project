from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import *
urlpatterns = [
    path("",home_page_teacher,name = "teacher_home_page"),
    path("add_lesson/",add_lesson,name = "add_lesson"),
    path("add_lesson_module/<classroom>",add_lesson_module,name = "add_lesson_module"),
    path("students_clasrooms/",students_classroom,name = "students_classroom"),
    path('students_list/<classroom>',students_list,name = "students_list"),
    path('student_info/<student>',Student_info,name = "student_info"),
    path("add_grade/",add_grade,name = "add_grade"),
    path("add_grade_year/<classroom>",add_grade_classroom_year,name = "add_grade_year"),
    path("add_grade_classroom/<classroom>",add_grade_classroom,name  = 'add_grade_classroom'),
    path("add_grade_student/<classroom_grade1><classroom>",add_grade_student,name = "add_grade_student"),
    path('add_grade_in/<classroom_grade>/<student1>',add_grade_form,name = "add_grade_in"),
    path("add_devoir/",add_devoir,name = "add_devoir"),
    path("add_devoir_form/<classroom>",add_devoir_form,name = "add_devoir_form"),
    path("lessons_posted/",lessons_posted,name = "lessons_posted"),
    path("lesson_update_form/<lesson_id>",lesson_update_form,name = "lesson_update_form"),
    path("grades_posted/",grade_posted,name = "grade_posted"),
    path("grade_update_form/<grade_id>",grade_update_form, name = 'grade_update_form'),
    path("search_for_student_form/<classroom>", search_for_student_form,name = 'search_for_student_form'),
    path("student_search_result/<first_name>/<last_name>",student_search_result,name = "student_result_query"),
    path("add_exam_alert_classroom/",add_exam_alert_classroom,name = "add_exam_alert_classroom"),
    path("add_exam_alert_form/<classroom>",add_exam_alert_form_view,name = 'add_exam_alert_form'),
    path("exam_alerts_posted/",exam_alerts_posted,name = "exam_alerts_posted"),
    path("edit_exam_alert_form/<id_form1>",edit_exam_alert_form,name = "edit_exam_alert_form")
    
]+static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)