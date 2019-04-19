from django.shortcuts import render, redirect
from .forms import FeedbackForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Student,Teacher,Course,Feedback

def HomePage(request):
    return render(request,'login.html')
def student_login(request):
    return render(request,'login_student.html')
def teacher_login(request):
    return render(request,'login_teacher.html')

def create_feedback(request):
    if request.method == "POST":
        form = FeedbackForm(request.POST)
        if form.is_valid():
            feedback = form.save(commit=False)
            feedback.save()
            return redirect('login.html')
    else:
        form = FeedbackForm()
    return render(request, 'feedback_create.html', {'form': form})
from django.shortcuts import render

def logIn(request):
    if request.user.is_authenticated():
        return redirect('/')
    if request.method == "post":
    	username = request.POST.get('username')
    	password = request.POST.get('password')
    	user = User.objects.filter(username=username)
    	user = authenticate(username=username, password=password)

    	if user:
    		student = Student.objects.filter(user=user)
    		if student.count() != 0:
    			login(request, user)
    			return redirect('create_feedback')
    		else:
    			return render(request, 'login_student.html', {'i': 'Invalid User SAP ID'})
    	else:
    		return render(request, 'login_student.html', {'i': 'Invalid Password/SAP ID'})

    return render(request, 'login_student.html', {'i': ''})
