from django import forms
from .models import Feedback, Course, Teacher

class FeedbackForm(forms.ModelForm):
    courseChoices =  (
        (course.course_code , course.course_code) 
        for data in Teacher.objects.all()
            for course in data.courses.all()
    )
    course_id = forms.ChoiceField(choices=courseChoices)
    
    class Meta:
        model = Feedback
        fields = ('teacher_id', 'course_id','skills', 'knowledge', 'interactivity', 'review')
