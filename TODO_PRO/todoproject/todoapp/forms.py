from .models import task
from django import forms
class form_todo(forms.ModelForm):
    class Meta:
        model=task
        fields=['task_name','priority','date']
