from collections import OrderedDict

from .models import Course, Lab, Profile, Teacher
from django import forms
from django.forms.fields import DateTimeField
from django.forms.widgets import SelectDateWidget, TimeInput

from landing.models import Student, Problem


class DateInput(forms.DateInput):
    input_type = 'date'


class AddCourseForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(AddCourseForm, self).__init__(*args, **kwargs)
        fields_keyOrder = ['code', 'name', 'target_batch', 'session']
        if 'keyOrder' in self.fields:
            self.fields.keyOrder = fields_keyOrder
        else:
            self.fields = OrderedDict(
                (k, self.fields[k]) for k in fields_keyOrder)
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
        fields = {'name', 'code', 'session', 'target_batch'}


class EditCourseForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(EditCourseForm, self).__init__(*args, **kwargs)
        fields_keyOrder = ['code', 'name', 'target_batch', 'session']
        if 'keyOrder' in self.fields:
            self.fields.keyOrder = fields_keyOrder
        else:
            self.fields = OrderedDict(
                (k, self.fields[k]) for k in fields_keyOrder)
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


class AddStudentForm(forms.Form):
    roll_no = forms.CharField(max_length=9)

    class Meta:
        fields = {'roll_no'}


class AddAssistantForm(forms.Form):
    roll_no = forms.CharField(max_length=9)

    class Meta:
        fields = {'roll_no'}


class AddLabForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(AddLabForm, self).__init__(*args, **kwargs)
        fields_keyOrder = ['id', 'date', 'start_time', 'end_time', 'description']
        if 'keyOrder' in self.fields:
            self.fields.keyOrder = fields_keyOrder
        else:
            self.fields = OrderedDict(
                (k, self.fields[k]) for k in fields_keyOrder)

        self.fields['id'].label = 'Lab ID'
        self.fields['date'].label = 'Date'
        self.fields['start_time'].label = "Start Time"
        self.fields['end_time'].label = "End Time"
        self.fields['description'].label = "Description"

        self.fields['id'].widget.attrs.update({
            'class': 'uk-input uk-width-auto',
            'placeholder': 'Eg: 2',
        })
        self.fields['description'].widget.attrs.update({
            'class': 'uk-textarea uk-input',
            'placeholder': 'Add description here',
        })
        self.fields['date'].widget.attrs.update({
            'class': 'uk-select uk-width-auto',
            'type': 'date'
        })
        self.fields['start_time'].widget.attrs.update({
            'class': 'uk-select uk-width-auto',
            'type': 'time'
        })
        self.fields['end_time'].widget.attrs.update({
            'class': 'uk-select uk-width-auto',
            'type': 'time'
        })

    class Meta:
        model = Lab
        fields = {'id', 'date', 'start_time', 'end_time', 'description'}
        widgets = {
            'date': SelectDateWidget(),
        }


class AddProblemForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(AddProblemForm, self).__init__(*args, **kwargs)
        fields_keyOrder = ['title', 'content']
        if 'keyOrder' in self.fields:
            self.fields.keyOrder = fields_keyOrder
        else:
            self.fields = OrderedDict(
                (k, self.fields[k]) for k in fields_keyOrder)
        self.fields['title'].label = 'Problem Title'
        self.fields['content'].label = 'Problem Content'

        self.fields['title'].widget.attrs.update({
            'class': 'uk-input',
            'placeholder': 'Problem - 1: Fibbonaci'
        })

        self.fields['content'].widget.attrs.update({
            'class': 'uk-input uk-textarea',
            'placeholder': 'You have ....'
        })

    class Meta:
        model = Problem
        fields = {'title', 'content'}
