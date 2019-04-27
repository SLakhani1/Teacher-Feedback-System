from django import forms
from .models import Feedback, Course, Teacher

class FeedbackForm(forms.ModelForm):
    # courseChoices =  (
    #         (data.course_code , data.course_code) 
    #         for data in Course.objects.all() #filter(semester=self.user.semester, department='IT')
    #             # for course in data.courses.all()
    #     )
    

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        #print(user)
        super(FeedbackForm, self).__init__(*args, **kwargs)
        self.fields['course'] = forms.ChoiceField(
            choices=[
                (data , data) 
                for data in Course.objects.filter(semester=user.student.semester, department=user.student.department)]
        )
        
    # course_id = forms.ChoiceField(choices=courseChoices)
    class Meta:
        model = Feedback
        fields = ('teacher_id','skills', 'knowledge', 'interactivity', 'review')