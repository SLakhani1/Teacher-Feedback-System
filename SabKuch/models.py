from django.db import models
from django.core.validators import MaxValueValidator
from django.db.models import Max, Min, Avg
from django.contrib.auth.models import User

class Course(models.Model):
    course_code = models.CharField(max_length=20, primary_key=True, blank = False)
    course_name = models.CharField(max_length=40, blank = False)
    semester = models.PositiveIntegerField(validators = [MaxValueValidator(10)], default=1)
    department = models.CharField(max_length=3, choices=( ('IT', 'IT'), ('ECE', 'ECE')), default="IT")
    ltp = models.PositiveIntegerField(validators = [MaxValueValidator(333)], blank = False)
    
    def __str__(self):
        return self.course_code

class Teacher(models.Model):
    user = models.OneToOneField(User)
    fac_code = models.CharField(primary_key=True,max_length=5, blank = False)
    first_name = models.CharField(max_length=20, blank = False)
    last_name = models.CharField(max_length=20, blank = False)
    designation = models.CharField(max_length=20 , blank = False)
    department = models.CharField(max_length=3, choices=( ('IT', 'IT'), ('ECE', 'ECE')), default="IT")
    courses = models.ManyToManyField(Course, blank = False, related_name='course_teacher')

    def __str__(self):
        return self.fac_code

class Student(models.Model):
    user = models.OneToOneField(User, related_name='student')
    #enrollment_id = models.CharField(max_length=20, primary_key=True)
    first_name = models.CharField(max_length=20, blank = False)
    last_name = models.CharField(max_length=20, blank = False)
    semester = models.PositiveIntegerField(validators = [MaxValueValidator(10)], blank = False)
    department = models.CharField(max_length=3, choices=( ('IT', 'IT'), ('ECE', 'ECE')), default="IT")

    def __str__(self):
        return self.user.username

class Feedback(models.Model):
    student_id = models.ForeignKey(Student,on_delete=models.CASCADE, blank = False)
    feedback_id = models.AutoField(primary_key=True,blank = False)
    teacher_id = models.ForeignKey(Teacher, on_delete=models.CASCADE, related_name='fac_codes', blank = False)
    course_id = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='course_codes', blank = False)
    skills = models.PositiveIntegerField(validators = [MaxValueValidator(5)], default = 1)
    knowledge  = models.PositiveIntegerField(validators = [MaxValueValidator(5)], default = 1)
    interactivity = models.PositiveIntegerField(validators = [MaxValueValidator(5)], default = 1)
    review = models.TextField(blank = False)

    def __str__(self):
        return str(self.feedback_id)

