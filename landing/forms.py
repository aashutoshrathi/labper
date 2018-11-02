from django import forms
from .models import Profile, Course, Teacher


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
