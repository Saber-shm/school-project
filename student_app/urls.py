from django.urls import path
from . import views
urlpatterns = [
    path("", views.home_page, name="student_home1"),
    path("lessons/", views.lessons_page, name="lessons"),
    path('pdf/download/<int:pdf_id>/', views.download_pdf, name='pdf_download'),
    path("error_lesson/", views.error_lesson, name="error_lesson"),
    path("lesson_module/<module_name>", views.lesson_module, name="lesson_module"),
    path("lesson_search/<result>",views.lesson_search,name = "lesson_search"),
    path("modules/",views.module_page,name = "module_page"),
    path("grades/",views.grade_year,name = "grade"),
    path("grade_semetre/",views.grade_semetre,name = "grade_semestre"),
    path("grades_view/<year>/<semestre>",views.grade_view,name = "grade_views"),
    path("lesson_page/<lesson_title>",views.lesson_page,name = "lesson_page"),
    path("myprofile/",views.myprofile_page,name = "myprofile_page"),
    path("devoir_list/",views.devoir_list,name ="devoir_list" ),
    path("devoir_view/<devoir_id>",views.devoir_view,name = "devoir_view"),
    path("timetable/",views.timetable_view,name = "timetable"),
    path("alert_exam/",views.alert_exam_list,name = "alert_exam_list"),
    path("exam_alert_view/<exam_id>",views.alert_exam_view,name = "alert_exam_view"),

]
