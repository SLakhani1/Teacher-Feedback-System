from django.shortcuts import render, redirect
from .forms import FeedbackForm

def HomePage(request):
    return render(request,'login.html')
<<<<<<< HEAD
def student_login(request):
    return render(request,'login_student.html')
def teacher_login(request):
    return render(request,'login_teacher.html')
=======

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
>>>>>>> 5193875c7e365ef7333f6836246882e5b31f0a85
