from news.models import Submission, Comment
from django.contrib.auth.models import User
from django import forms

class SubmissionForm(forms.ModelForm):
    author = forms.ModelChoiceField(
            queryset=User.objects.all(),
            widget = forms.HiddenInput(),
            required = False
            )

    class Meta:
        model = Submission
        exclude = ('created_at', 'upvotes')


class CommentForm(forms.ModelForm):
    submission = forms.ModelChoiceField(
            queryset=Submission.objects.all(),
            widget = forms.HiddenInput(),
            required = False
            )

    
    class Meta:
        model = Comment
        exclude = ('last_modified', 'parent')
