from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from main.models import *

# Create your views here.

def login_user(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request,user)
            try:
                user_info = Student.objects.get(user=request.user)
                return redirect("student_home1")
            except:
                try: 
                     user_info = Teacher.objects.get(user=request.user)
                     return redirect("teacher_home_page")
                except:
                    try:
                        user_info = Monitor.objects.get(user = request.user)
                        return redirect('monitors_home_page')
                    except:
                        return redirect("logins")

        else:
            messages.success(request,'problem try again')
            return redirect("logins")
        
    return render(request,"login_user.html",{})    

def success(request):
    return redirect("home")

def logout_user(request):
    print(request.user)
    logout(request)
    
    return redirect("logins")
def register_user(request):
	if request.method  =="POST":
		form = UserCreationForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data["username"]
			password = form.cleaned_data["password1"]
			user = authenticate(username = username,password = password)
			login(request, user)
			return redirect("success")
	else:
		form = UserCreationForm()
	return render(request,"register_user.html",{"form":form})
