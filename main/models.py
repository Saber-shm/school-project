from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


class messages_contact(models.Model):
    first_name = models.CharField(max_length=120)
    last_name = models.CharField(max_length=120)
    email = models.EmailField(blank=True)
    phone_number = models.CharField(max_length=50, blank=True)
    message = models.TextField()

    def __str__(self):
        return self.first_name + " " + self.last_name
class Year_study(models.Model):
    years = models.CharField(max_length=120)
    def __str__(self):
        return str(self.years)
class Education_level(models.Model):
    name = models.CharField(max_length=120)

    def __str__(self):
        return self.name
class Level(models.Model):
    level = models.CharField(max_length=120)
    education_level = models.ForeignKey(Education_level,on_delete=models.SET_NULL,null = True,blank = True)
    year_study = models.ForeignKey(Year_study,on_delete=models.CASCADE,null = True,blank = True)
    def __str__(self):
        return self.level
class Semestre(models.Model):
    semestre = models.CharField(max_length=120)
    def __str__(self):
        return self.semestre
class Module(models.Model):
    name = models.CharField(max_length=120)
    level = models.ManyToManyField(Level,blank = True)
    year_study = models.ForeignKey(Year_study,on_delete=models.CASCADE,null = True,blank = True)
    def __str__(self):
        return str(self.name)
    
class Classroom(models.Model):
    name = models.CharField(max_length= 120)
    level = models.ForeignKey(Level,on_delete=models.CASCADE)
    modules = models.ManyToManyField(Module)
    year_of_study = models.ForeignKey(Year_study,on_delete= models.CASCADE,null = True,blank = True)
    def __str__(self):
        return str(self.level) + " " + str(self.name)

    
class Classroom_grade(models.Model):
    classroom = models.ForeignKey(Classroom,on_delete=models.CASCADE)
    semestre = models.ForeignKey(Semestre,on_delete=models.CASCADE,null = True)
    year_study = models.ForeignKey(Year_study,on_delete=models.CASCADE)

    def __str__(self):
        return str(self.classroom) + ' ' + str(self.year_study) + " Semestre " + str(self.semestre)

class Student(models.Model):    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    level =models.ForeignKey(Level,on_delete=models.SET_NULL,null = True,blank = True)
    classroom = models.ForeignKey(Classroom,on_delete=models.SET_NULL,null = True,blank = True)
    first_name = models.CharField(max_length=120,blank = True)
    last_name = models.CharField(max_length=120,blank = True)
    birthday = models.DateField(blank=True)
    mothers_full_name = models.CharField(max_length=120,blank = True)
    father_full_name = models.CharField(max_length=120,blank = True)
    mother_email = models.EmailField(blank = True)
    father_email = models.EmailField(blank = True)
    mother_phone_number = models.CharField(max_length=120)
    father_phone_number = models.CharField(max_length=120)
    adress = models.CharField(max_length=300,blank = True)
    year_study = models.ForeignKey(Year_study,on_delete=models.SET_NULL,null = True,blank = True)
    image = models.ImageField(null = True,blank = True,upload_to="images/")
    
    def __str__(self):
        return self.user.username


class Teacher(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    classroom =models.ManyToManyField(Classroom)
    module = models.ForeignKey(Module,on_delete=models.SET_NULL,null = True,blank = True)
    first_name = models.CharField(max_length=120)
    last_name = models.CharField(max_length=120)
    phone_number = models.CharField(max_length=120)
    email = models.EmailField()
    year_study = models.ForeignKey(Year_study,on_delete=models.CASCADE,null = True,blank = True)
    image = models.ImageField(null = True,blank = True,upload_to="images/")

    def __str__(self):
        return str(self.user.username)

class Monitor(models.Model):
    user = models.ForeignKey(User,models.CASCADE)
    first_name = models.CharField(max_length=120)
    last_name = models.CharField(max_length=120)
    phone_number = models.CharField(max_length=120)
    email = models.EmailField()
    year_study = models.ForeignKey(Year_study,on_delete=models.CASCADE,null = True,blank = True)
    image = models.ImageField(null = True,blank = True,upload_to="images/")

    def __str__(self):
        return self.user.username




class Lesson(models.Model):
    title = models.CharField(max_length=200)
    classroom = models.ForeignKey(Classroom,on_delete=models.SET_NULL,null = True,blank = True)
    file = models.FileField(upload_to='pdf_files/')
    module = models.ForeignKey(Module,on_delete=models.SET_NULL,null = True,blank = True)
    teacher = models.ForeignKey(Teacher,on_delete=models.SET_NULL,null = True,blank = True)
    description = models.TextField(blank = True,null = True)
    year_study = models.ForeignKey(Year_study,on_delete=models.CASCADE,null = True,blank = True)
    def __str__(self):
        return str(self.title)


class Grade(models.Model):
    exams_choices=    [
        ('exam 1','Exam 1'),
        ('exam 2','Exam 2'),
        ('exam 3','Exam 3'),
        ('exam 4','Exam 4'),
    ]

    student = models.ForeignKey(Student,on_delete=models.CASCADE)
    module = models.ForeignKey(Module,on_delete=models.CASCADE)
    note = models.FloatField()
    classroom_grade = models.ForeignKey(Classroom_grade,on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teacher,on_delete=models.SET_NULL,null = True,blank = True)
    exam = models.CharField(max_length=120,choices=exams_choices,default="exam 1")
    def __str__(self):
        return str(self.classroom_grade)+ " " +str(self.student)+ " " + str(self.module)
    
class Homework(models.Model):
    post_date = models.DateField(auto_now=True)
    title = models.CharField(max_length= 120    )
    descriptions = models.TextField()
    deadline = models.DateField("deadline")
    classroom = models.ForeignKey(Classroom,on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teacher,on_delete=models.SET_NULL,null = True,blank = True)
    year_study = models.ForeignKey(Year_study,on_delete=models.CASCADE,null = True,blank = True)
    module = models.ForeignKey(Module,on_delete=models.CASCADE,null = True,blank = True)
    def __str__(self):
        return str(self.module) +" to "+str(self.deadline)

class Attendence_report(models.Model):
    student = models.ForeignKey(Student,on_delete=models.SET_NULL,null = True,blank = True)
    classroom = models.ForeignKey(Classroom,on_delete=models.SET_NULL,null = True)
    date = models.DateField()
    m1 = models.BooleanField(default=True)    
    m2 = models.BooleanField(default=True)    
    m3 = models.BooleanField(default=True)    
    m4 = models.BooleanField(default=True)    
    e1 = models.BooleanField(default=True)
    e2 = models.BooleanField(default=True)
    e3 = models.BooleanField(default=True)
    e4 = models.BooleanField(default=True)
    def __str__(self):
        return str(self.classroom) + ' '+  str(self.date)

class Timetable(models.Model):
    days = [
    ("lundi", "Lundi"),
    ("mardi", "Mardi"),
    ("mercredi", "Mercredi"),
    ("jeudi", "Jeudi"),
    ("vendredi", "Vendredi"),
    ("samedi", "Samedi"),
    ("dimanche", "Dimanche")
    ]
    classroom = models.ForeignKey(Classroom,on_delete=models.CASCADE)
    year_study = models.ForeignKey(Year_study,on_delete=models.CASCADE)
    p1 = models.ForeignKey(Module, on_delete=models.CASCADE, related_name='timetable_p1',blank=True,null=True)
    p2 = models.ForeignKey(Module, on_delete=models.CASCADE, related_name='timetable_p2',blank=True,null=True)
    p3 = models.ForeignKey(Module, on_delete=models.CASCADE, related_name='timetable_p3',blank=True,null=True)
    p4 = models.ForeignKey(Module, on_delete=models.CASCADE, related_name='timetable_p4',blank=True,null=True)
    p5 = models.ForeignKey(Module, on_delete=models.CASCADE, related_name='timetable_p5',blank=True,null=True)
    p6 = models.ForeignKey(Module, on_delete=models.CASCADE, related_name='timetable_p6',blank=True,null=True)
    
    lunch_break = models.CharField(max_length=120)

    posted_by = models.ForeignKey(User,on_delete= models.SET_NULL,null = True ,blank = True)
    day = models.CharField(max_length=120,choices=days)

    def __str__(self):
        return str(self.classroom) + " " + str(self.year_study)
    
class Exam_alert(models.Model):
    date = models.DateField()
    posted_by = models.ForeignKey(User,on_delete=models.CASCADE)
    module = models.ForeignKey(Module,on_delete=models.CASCADE)
    lessons = models.TextField()
    year_study = models.ForeignKey(Year_study,on_delete=models.CASCADE)
    classroom = models.ForeignKey(Classroom,on_delete=models.CASCADE,null = True,blank = True)
    
    def __str__(self):
        return str(self.date)+ " " + str(self.module) + " " + str(self.year_study)