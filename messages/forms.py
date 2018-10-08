from django import forms
from .models import Message


class MessageForm(forms.Form):
    title = forms.CharField()
    count = forms.CharField()
    description = forms.IntegerField()

