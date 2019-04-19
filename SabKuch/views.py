from django.shortcuts import render, redirect
from .forms import FeedbackForm
from .models import Student, Course, Feedback, Teacher

def HomePage(request):
    return render(request,'login.html')
<<<<<<< HEAD
def student_login(request):
    return render(request,'login_student.html')
def teacher_login(request):
    return render(request,'login_teacher.html')
=======

def create_feedback(request):
<<<<<<< HEAD
    if request.user.is_authenticated():

    #     username = request.user
    #     user = Student.objects.filter(user=username)[0]

    #     sub1 = Course.objects.filter(semester=user.semester, department=user.department[0])
    #     sub2 = Course.objects.filter(semester=user.semester, department=user.department)
    #     courses = sub1.union(sub2)
    #     print(courses)

    #     #user.subject = courses
    #     user.save()

    #     fname = user.first_name
    #     lname = user.last_name
    #     email = request.user.email
    #     semester = user.semester
    #     department = user.department
    #     # subject_list = [i.name for i in user.subject.all()]
    #     course_list = courses

    #     # feeds = Feedback.objects.filter(student_id=user.enrollment_id)
    #     # subjects_done_feedback = [i.subject.name + '-' + i.teacher.fname + ' ' + i.teacher.lname for i in f]

    #     # print("Subject done feedback: ", (subjects_done_feedback))

    #     # print("Subject List: ", subject_list)
    #     # teacher_list = TeacherProfile.objects.all()

    #     # subject_teacher_list = []
    #     # for i in teacher_list:
    #     #     for j in i.subject.filter(semester=user.semester):
    #     #         subject_teacher_list.append(j.name + '-' + i.fname + ' ' + i.lname)

    #     # subject_list = [i.split('-')[0] for i in subject_teacher_list if i not in subjects_done_feedback]
    #     # final_names = [i.name for i in final]
    #     # unique_sub_list = []
    #     # for x in subject_list:
    #     #     if x not in unique_sub_list:
    #     #         unique_sub_list.append(x)
    #     # subject_list = unique_sub_list

        


    #     # print("Subjects not feedback: " + str(subject_list))
    #     if request.POST:
    #         if request.POST.get('fname'):
    #             fname = request.POST.get('fname')
    #             lname = request.POST.get('lname')
    #             email = request.POST.get('email')
    #             semester = request.POST.get('semester')
    #             department = request.POST.get('department')
    #             user = UserProfile.objects.filter(user=request.user)[0]
    #             if user.department != department:
    #                 Feedback.objects.filter(student_id=user).delete()
    #             user.fname = fname
    #             user.lname = lname
    #             user.semester = semester
    #             user.department = department
    #             sub1 = Course.objects.filter(semester=user.semester, department=user.department[0])
    #             sub2 = Course.objects.filter(semester=user.semester, department=user.department)
    #             courses = sub1.union(sub2)

    #             user.course = courses
    #             user.course = Course.objects.filter(semester=semester)
    #             request.user.email = email

    #             request.user.save()
    #             user.save()

    #             return redirect('/')
    #         else:
    #             u = user
    #             s = request.POST.get('subject')
    #             t = request.POST.get('teacher')
    #             f1 = request.POST.get('f1')
    #             f2 = request.POST.get('f2')
    #             f3 = request.POST.get('f3')
    #             review = request.POST.get('review')

    #             if s == "Select a Subject" or t == None:
    #                 return redirect('/')
    #             tea = Teacher.objects.filter(fname=t.split(" ")[0])
    #             print(tea)
    #             sub = Course.objects.filter(name=s, batch=u.batch)
    #             if sub.count() == 0:
    #                 sub = Course.objects.filter(name=s, batch=u.batch[0])
    #             print(sub)
    #             f = Feedback.objects.create(
    #                 student=u,
    #                 subject=sub[0],
    #                 teacher=tea[0],
    #                 res1=f1,
    #                 res2=f2,
    #                 res3=f3,
    #                 sug=sug
    #             )
    #             f.save()
    #             return redirect('analytics')
    #     context = {
    #         'fname': fname,
    #         'lname': lname,
    #         'email': email,
    #         'semester': semester,
    #         'department': batch,
    #         'batches': ['A' + str(i) for i in range(1, 5)] + ['B' + str(i) for i in range(1, 5)],
    #         'numbers': [i for i in range(3, 9)],
    #         'teacher_list': teacher_list,
    #         'subject_list': subject_list
    #     }
    #     return render(request, 'appOne/dashboard.html', context)
    # else:
    #     return redirect('signup')

        if request.method == "POST":
            form = FeedbackForm(request.POST)
            if form.is_valid():
                feedback = form.save(commit=False)
                feedback.save()
                return redirect('login.html')
        else:
            form = FeedbackForm()
        return render(request, 'feedback_create.html', {'form': form})
=======
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
>>>>>>> 5b5260392cda4bbaa57de0f771d1d7de9bb2da84
