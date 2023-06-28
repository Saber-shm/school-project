from django.urls import path
from . import views

urlpatterns =[
    path("",views.login_user,name  = "logins"),
    path("success/",views.success,name = "success"),
    path("logout_user/",views.logout_user,name = "logoutt"),
    path("register",views.register_user,name  = "registerr")
]   