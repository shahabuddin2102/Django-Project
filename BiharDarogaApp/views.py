from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Student
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout

# Create your views here.

def home_page(request):
    return render(request, 'home.html', {})

def about_page(request):
    return render(request, 'about.html', {})

def career_page(request):
    return render(request, 'career.html', {})

def course_page(request):
    return render(request, "course.html", {})

def header_page(request):
    return render(request, "header.html", {})

def footer_page(request):
    return render(request, "footer.html", {})

def nav_page(request):
    return render(request, 'nav.html', {})

def addmission_page(request):
    
    #data fetch
    if request.method=='POST':
        fullname=request.POST.get('fullname')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        cname=request.POST.get('cname')
        password=request.POST.get('password')

        #create object
        student=Student()
        student.fullname=fullname
        student.email=email
        student.phone=phone
        student.coursename=cname
        student.password=password

        #savet data
        student.save()

        return redirect("/course/")

    return render(request, "addmission.html", {})

def student_data_page(request):
    students=Student.objects.all()
    return render(request, 'student.html', context={'details': students})
