from django import forms
from .models import FeedLink

class AddFeedForm(forms.ModelForm):
    class Meta:
        model = FeedLink
        fields = ['link',]


