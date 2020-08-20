from django import forms
from django.forms.models import inlineformset_factory
from .models import Course, Module, Content


ModuleFormSet = inlineformset_factory(Course,Module,
                                        fields=['title', 'description'],
                                        extra=2,
                                        can_delete=True)

class ContentForm(forms.ModelForm):
    class Meta:
        model = Content
        fields = ('title', 'summary', 'body')