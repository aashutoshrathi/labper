from .models import Course, Profile, Teacher
from django import forms

from landing.models import Student


class AddCourseForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(AddCourseForm, self).__init__(*args, **kwargs)
        self.fields['name'].label = 'Course Name'
        self.fields['code'].label = 'Course Code'

        self.fields['name'].widget.attrs.update({
            'class': 'uk-input',
            'placeholder': 'Introduction to Example Technology'
        })
        self.fields['code'].widget.attrs.update({
            'class': 'uk-input uk-width-auto',
            'placeholder': 'CSX0X or ITX0X'
        })

        self.fields['target_batch'].widget.attrs.update({
            'class': 'uk-input uk-width-auto',
        })

        self.fields['session'].widget.attrs.update({
            'class': 'uk-select uk-width-auto',
            'placeholder': '20XX-XY'
        })

    class Meta:
        model = Course
        fields = ('name', 'code', 'session', 'target_batch')


class EditCourseForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(EditCourseForm, self).__init__(*args, **kwargs)
        self.fields['name'].label = 'Course Name'
        self.fields['code'].label = 'Course Code'

        self.fields['name'].widget.attrs.update({
            'class': 'uk-input',
        })

        self.fields['code'].widget.attrs.update({
            'class': 'uk-input uk-width-auto',
        })

        self.fields['target_batch'].widget.attrs.update({
            'class': 'uk-input uk-width-auto',
        })

        self.fields['session'].widget.attrs.update({
            'class': 'uk-select uk-width-auto',
        })

    class Meta:
        model = Course
        fields = {'name', 'code', 'session', 'target_batch'}


class AddStudentForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(AddStudentForm, self).__init__(*args, **kwargs)
        self.fields['profile'].label = 'Student'
        self.fields['profile'].widget.attrs.update({
            'class': 'uk-select uk-width-auto',
        })

    class Meta:
        model = Student
        fields = {'profile'}


class AddLabForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(AddLabForm, self).__init__(*args, **kwargs)
        self.fields['id'].label = 'Lab ID'
        self.field['date'].label='Date'
        self.field['start_time'].label="Start Time"
        self.field['end_time'].label="End Time"

        self.fields['id'].widget.attrs.update({
            'class': 'uk-input',
            'placeholder': 'Write 2 for Lab 2'
        })
        self.fields['date'].widget.attrs.update({
            'class': 'uk-input'
        })
        self.fields['start_time'].widget.attrs.update({
            'class': 'uk-input',
        })
        self.fields['end_time'].widget.attrs.update({
            'class': 'uk-input',
        })
    class Meta:
        model = Lab
        fields = ('id', 'date', 'start_time', 'end_time')

