from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect


@login_required
def home(request):
    return render(request, 'landing/home.html')


def land(request):
    return render(request, 'landing/base.html')


# only4 testing
def test_func():
    return True
