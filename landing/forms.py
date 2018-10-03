from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import CheckboxSelectMultiple

from .models import Profile

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(label="Hospital Name", max_length=30, required=False, help_text='Enter Hospital Name '
                                                                                                 'here')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'password1', 'password2')


class UsernameForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(UsernameForm, self).__init__(*args, **kwargs)
        self.fields['username'].label = 'New Username'
        self.fields['username'].widget.attrs.update({
            'class': 'uk-input uk-width-auto',
            'placeholder': 'New Username'
        })

    class Meta:
        model = User
        fields = {'username'}
