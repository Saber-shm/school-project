from django.shortcuts import render,redirect
from .forms import messages_contact_form
from .models import *
from django.http import HttpResponseRedirect
# Create your views here.

def home_page(request):
    if request.user.is_authenticated:
        try:
            user_info = Student.objects.get(user=request.user)
            return redirect("student_home1")
        except:
            try: 
                    user_info = Teacher.objects.get(user=request.user)
                    return redirect("teacher_home_page")
            except:
                    return redirect("login")
    return render(request, "home.html")

def contact_form(request):
    submitted = False
    if request.method == "POST":
        form = messages_contact_form(request.POST)
        if form.is_valid():
            form.save()

            return HttpResponseRedirect("/contact?submitted=True")
    else:
        form = messages_contact_form
        if "submitted" in request.GET:
            submitted = True

    return render(request,"contact.html",{"form":form,"submitted":submitted})
