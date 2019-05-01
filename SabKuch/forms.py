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
            widget=forms.Select(attrs = {'class':'selectbox'}),
            choices=[
                (data , data) 
                for data in Course.objects.filter(semester=user.student.semester, department=user.student.department)]
        )   


        self.fields['skills'] = forms.ChoiceField(
            widget=forms.RadioSelect(attrs = {}),
            choices=[
                ('1', 'Poor',), ('2', 'Good',), ('3', 'Very Good',), ('4', 'Excellent',), ('5', 'Awesome',)]
        )


        self.fields['knowledge'] = forms.ChoiceField(
            widget=forms.RadioSelect(attrs = {}),
            choices=[
               ('1', 'Poor',), ('2', 'Good',), ('3', 'Very Good',), ('4', 'Excellent',), ('5', 'Awesome',)]
        )


        self.fields['interactivity'] = forms.ChoiceField(
            widget=forms.RadioSelect(attrs = {}),
            choices=[
               ('1', 'Poor',), ('2', 'Good',), ('3', 'Very Good',), ('4', 'Excellent',), ('5', 'Awesome',)]
        )
        
    # course_id = forms.ChoiceField(choices=courseChoices)
    class Meta:
        model = Feedback
        fields = ('teacher_id','skills', 'knowledge', 'interactivity', 'review')
        widgets = {
            
            'course':forms.Select(attrs = {'class':'selectbox'}),
            'teacher_id':forms.Select(attrs = {'class':'selectbox'}),
            'review': forms.Textarea(attrs={'class':'form-control','rows':'3'}),


        }