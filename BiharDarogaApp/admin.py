from django.contrib import admin
from .models import Student

# Register your models here.

class StudentAdmin(admin.ModelAdmin):
    list_display=('fullname', 'email', 'phone', 'coursename', 'password')

admin.site.register(Student, StudentAdmin)

#usename:- shahabuddin_developer
#password:- 123456789
