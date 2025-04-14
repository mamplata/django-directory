# projectmanager/forms.py
from django import forms
from .models import Project, Task


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['name', 'description']


class TaskForm(forms.ModelForm):
    due_date = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'}),
        required=False  # matches your model field settings: null=True, blank=True
    )

    class Meta:
        model = Task
        fields = ['title', 'description', 'is_completed', 'due_date']
