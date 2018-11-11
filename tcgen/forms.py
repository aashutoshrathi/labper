from django import forms
from tcgen.models import TestCase


class DocumentForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(DocumentForm, self).__init__(*args, **kwargs)
        self.fields['code_file'].label = 'Correct Code file'

        self.fields['code_file'].widget.attrs.update({
            'class': 'uk-input uk-width-auto',
            'type': 'file'
        })

    class Meta:
        model = TestCase
        fields = {'code_file', }
