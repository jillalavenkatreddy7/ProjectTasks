"""Provider_for_project2 URL Configuration

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

urlpatterns = [
    path('admin/', admin.site.urls),
    path('user_registration/',views.UserRegister.as_view()),
    path('login_check/',views.Login_check.as_view()),
    path('user_req_save/',views.User_req_save.as_view()),
    path('my_requests/<str:email>/',views.My_requests.as_view()),
    path('forgot_save/',views.Forgot_save.as_view()),
]
