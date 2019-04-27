from django.shortcuts import render, redirect
from .forms import FeedbackForm
from .models import Student, Course, Feedback, Teacher
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate

def HomePage(request):
    return render(request,'login.html')

def student_login(request):
    if request.user.is_authenticated():
        return redirect('/')
    if request.method == "POST":
    	username = request.POST.get('username')
    	password = request.POST.get('password')
    	user = User.objects.filter(username=username)
    	user = authenticate(username=username, password=password)

    	if user:
            print("Hello")
            student = Student.objects.filter(user=user)
            if student.count() != 0:
                login(request, user)
                return redirect('create_feedback')
            else:
                return render(request, 'login_student.html', {'i': 'Invalid User SAP ID','username': 'username'})
    	else:
    		return render(request, 'login_student.html', {'i': 'Invalid Password/SAP ID','username': 'username'})

    return render(request, 'login_student.html', {'i': '',,'username': 'username'})

def teacher_login(request):
    if request.user.is_authenticated():
        return redirect('/')
    if request.method == "POST":
    	username = request.POST.get('username')
    	password = request.POST.get('password')
    	user = User.objects.filter(username=username)
    	user = authenticate(username=username, password=password)

    	if user:
            teacher = Teacher.objects.filter(user=user)
            if teacher.count() != 0:
                login(request, user)
                return redirect('create_feedback')
            else:
                return render(request, 'login_teacher.html', {'i': 'Invalid User SAP ID', 'username': 'username'})
    	else:
    		return render(request, 'login_teacher.html', {'i': 'Invalid Password/SAP ID', 'username': 'username'})

    return render(request, 'login_teacher.html', {'i': '', 'username': 'username'})

def create_feedback(request):

    if request.user.is_authenticated():
    #     #if request.user.is_superuser:
    #     #    return redirect("admin_analytics")
    #     #elif is_teacher(request.user):
    #     #    return redirect('teacher_analytics')
        
        #print(request.user)
        if request.method == "POST":
            form = FeedbackForm(request.POST, user=request.user)
            if form.is_valid():
                feedback = form.save(commit=False)
                feedback.student_id = request.user.student
                feedback.save()
                return redirect('login.html')
        else:
            form = FeedbackForm(user=request.user)
        return render(request, 'feedback_create.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect("/")
