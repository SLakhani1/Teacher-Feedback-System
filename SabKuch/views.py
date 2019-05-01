from django.shortcuts import render, redirect , get_object_or_404
from .forms import FeedbackForm
from .models import Student, Course, Feedback, Teacher
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.http import HttpResponse

def HomePage(request):
    if request.user.is_authenticated() and request.user.student:
        return redirect('dashboard_student')
    # elif request.user.is_authenticated():
    #     return redirect('dashboard_teacher')
    if request.method == "POST" and request.POST.get('id')=="1":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = User.objects.filter(username=username)
        user = authenticate(username=username, password=password)

        if user:
            print("Hello")
            student = Student.objects.filter(user=user)
            if student.count() != 0:
                login(request, user)
                return redirect('dashboard_student')
            else:
                return render(request, 'login.html', {'i': 'Invalid User SAP ID','username': 'username'})
        else:
            return render(request, 'login.html', {'i': 'Invalid Password/SAP ID','username': 'username'})

    if request.method == "POST" and request.POST.get('id')=="2":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = User.objects.filter(username=username)
        user = authenticate(username=username, password=password)

        if user:
            teacher = Teacher.objects.filter(user=user)
            if teacher.count() != 0:
                login(request, user)
                return redirect('dashboard_teacher')
            else:
                return render(request, 'login.html', {'i': 'Invalid User SAP ID', 'username': 'username'})
        else:
            return render(request, 'login.html', {'i': 'Invalid Password/SAP ID', 'username': 'username'})
    return render(request,'login.html')

def dashboard_student(request):
    if request.user.is_authenticated():
            return render(request, 'dashboard_student.html', {'username':request.user.username})
def dashboard_teacher(request):
    if request.user.is_authenticated():
            return render(request, 'dashboard_teacher.html', {'username':request.user.username})

def teachers_detail2(request,slug):
    if request.user.is_authenticated():
            teachers = get_object_or_404(Teacher, fac_code=slug)
            return render(request, 'teachers_detail2.html', {'teachers' : teachers,'username':request.user.username})

def teachers_detail3(request,slug):
    if request.user.is_authenticated():
            teachers = get_object_or_404(Teacher, fac_code=slug)
            return render(request, 'teachers_detail3.html', {'teachers' : teachers,'username':request.user.username})

def view_feedback(request):
    teachers = Teacher.objects.all()
    return render(request, 'view_feedback.html', {'teachers' : teachers,'username':request.user.username})

def view_feedback2(request):
    teachers = Teacher.objects.all()
    return render(request, 'view_feedback2.html', {'teachers' : teachers,'username':request.user.username})

def feedback_form(request):
    if request.user.is_authenticated():
    #     #if request.user.is_superuser:
    #     #    return redirect("admin_analytics")
    #     #elif is_teacher(request.user):
    #     #    return redirect('teacher_analytics')
        
        #print(request.user)

        if request.method == "POST":
            form = FeedbackForm(request.POST, user=request.user)
            if form.is_valid():
                course_id = request.POST.get('course')
                faculty_id = request.POST.get('teacher_id')
                if faculty_id==str(Teacher.objects.filter(courses=course_id)[0]):
                    print('Valid form')
                    feedback = form.save(commit=False)
                    feedback.course_id = Course.objects.filter(course_code=course_id)[0]
                    
                    feedback.student_id = request.user.student
                    temp = Feedback.objects.filter(teacher_id = faculty_id, course_id=course_id, student_id=request.user.student)
                    if(temp.count() == 0):
                        feedback.save()
                        return redirect('dashboard_student')
                    else:
                        return HttpResponse('You have already provided the feedback for this teacher')
                else:
                    return HttpResponse("The course selected by you isn't taught by the selected teacher")
        else:
            form = FeedbackForm(user=request.user)
            return render(request, 'form.html', {'form': form , 'username':request.user.username})


def teachers_detail(request):
   if request.user.is_authenticated():
       teachers = get_object_or_404(Teacher, fac_code=request.user.username)
       return render(request, 'teachers_detail.html', {'teachers' : teachers, 'username':request.user.username})


def logout_view(request):
    logout(request)
    return redirect("/")
