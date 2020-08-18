"""Project2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app import views
from django.views.generic import TemplateView
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.login),
    path('register/',TemplateView.as_view(template_name="register.html"),name='register'),
    path('register_save/',views.register_save,name='register_save'),
    path('login_check/',views.login_check,name='login_check'),
    path('req/',views.req,name='req'),
    path('req_save/',views.req_save,name='req_save'),
    path('myreq/',views.myreq,name='myreq'),
    path('forgot/',views.forgot,name='forgot'),
    path('forgot_save/',views.forgot_save,name='forgot_save'),
]
