from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.shortcuts import redirect, render
from urllib3 import request

from tcgen.forms import DocumentForm
from tcgen.generator import generate


def create_tc(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = DocumentForm()
    return render(request, 'tc_gen.html', {
        'form': form,
        'form_title': "Test Case Generator",
        'button': "Upload file",
    })
