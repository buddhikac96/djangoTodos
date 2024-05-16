from django import forms
from django.forms import ModelForm

from .models import Todo


class TodoForm(ModelForm):
    class Meta:
        model = Todo
        fields = ['title', 'description', 'completed']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'completed': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }
