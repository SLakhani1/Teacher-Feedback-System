from django.db import models
from django.core.validators import MaxValueValidator
from django.db.models import Max, Min, Avg


class Teacher(models.Model):
    fac_code = models.CharField(primary_key=True,max_length=5)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    designation = models.CharField(max_length=20)
    department = models.CharField(max_length=10)

    def __str__(self):
        return self.fac_code

class Student(models.Model):
    enrollment_id = models.CharField(max_length=20, primary_key=True)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    degree = models.CharField(max_length=20)
    joining_year = models.DateField()

    def __str__(self):
        return self.enrollment_id
    
class Course(models.Model):
    course_code = models.CharField(max_length=20, primary_key=True)
    course_name = models.CharField(max_length=40)
    session = models.CharField(max_length=20)
    ltp = models.PositiveIntegerField(validators = [MaxValueValidator(333)])
    
    def __str__(self):
        return self.course_code

class Feedback(models.Model):
    feedback_id = models.AutoField(primary_key=True)
    teacher_id = models.ForeignKey('teachers.Teacher', on_delete=models.CASCADE, related_name='fac_codes')
    course_id = models.ForeignKey('teachers.Course', on_delete=models.CASCADE, related_name='course_codes')
    field1 = models.PositiveIntegerField(validators = [MaxValueValidator(5)])
    field2 = models.PositiveIntegerField(validators = [MaxValueValidator(5)])
    field3 = models.PositiveIntegerField(validators = [MaxValueValidator(5)])
    comment1 = models.TextField()
    comment2 = models.TextField()

    def __str__(self):
        return str(self.feedback_id)

