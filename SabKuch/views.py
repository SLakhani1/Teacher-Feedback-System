from django.shortcuts import render

# Create your views here.

def HomePage(request):
    return render(request,'login.html')
def student_login(request):
    return render(request,'login_student.html')
def teacher_login(request):
    return render(request,'login_teacher.html')
