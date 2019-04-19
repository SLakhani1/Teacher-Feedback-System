from django.shortcuts import render, redirect
from .forms import FeedbackForm

def create_feedback(request):
    if request.method == "POST":
        form = FeedbackForm(request.POST)
        if form.is_valid():
            feedback = form.save(commit=False)
            feedback.save()
            return redirect(pass)
    else:
        form = FeedbackForm()
    return render(request, 'feedback_create.html', {'form': form})
