from django import forms
from .models import Feedback, Course

class FeedbackForm(forms.ModelForm):
    courseChoices =  (
        #(data.course_code , data.course_code) for data in Course.objects.all()
        ('sagar', 'sagar'),
        ('lakhani', 'lakhani')
    )
    course_id = forms.ChoiceField(choices=courseChoices)
    class Meta:
        model = Feedback
        fields = ('teacher_id', 'course_id','skills', 'knowledge', 'interactivity', 'review')
