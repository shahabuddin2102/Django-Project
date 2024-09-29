"""
URL configuration for BiharDarogaProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path,include
from BiharDarogaApp import views

urlpatterns = [
    path("",views.home_page, name="home"),
    path("about/",views.about_page, name="about"),
    path("career/",views.career_page, name="career"),
    path("course/",views.course_page, name="course"),
    path("header/",views.header_page, name="header"),
    path("footer/",views.footer_page, name="footer"),
    path("addmission/",views.addmission_page, name="addmission"),
    path("student/",views.student_data_page, name="student"),
    path("nav/",views.nav_page, name="nav"),
    path('admin/', admin.site.urls),
]
