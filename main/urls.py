from django.urls import path 
from django.conf import settings
from django.conf.urls.static import static

from . import views


urlpatterns = [
    path("",views.home_page,name = "home"),
    path("contact/",views.contact_form)
]