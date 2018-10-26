from django import forms
from .models import Profile, Course, Teacher


class DateInput(forms.DateInput):
    input_type = 'date'


class AddCourse(forms.ModelForm):
    class Meta:
        model = Course
        fields = ('name', 'code', 'session')
