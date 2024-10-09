from django import forms
from django.forms import TextInput

from .models import Messages

class MessageForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'contact__section-input', 'placeholder': 'Имя'
    }))
    email = forms.CharField(widget=forms.EmailInput(attrs={
        'class': 'contact__section-input', 'placeholder': 'email'
    }))
    message = forms.CharField(widget=forms.TextInput(attrs={
        'name': 'message', 'class': 'contact__section-message'
    }))

    class Meta:
        model = Messages
        fields = ('name', 'email', 'message')

