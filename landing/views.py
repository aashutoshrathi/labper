from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import Profile, Teacher
from django.http import JsonResponse


@login_required
def home(request):
    x = request.user
    target = Profile.objects.get(user=x)
    upgradable = False
    if not target.user.username.isdigit():
        upgradable = True
    return render(request, 'landing/home.html', {'upgd': upgradable})


@login_required
def upgrade(request):
    current = request.user
    target = Profile.objects.get(user=current)
    if not target.user.username.isdigit():
        make_teacher, create = Teacher.objects.get_or_create(profile=target)
    else:
        data = {
            'error': "Forbidden",
            'description': "Not for you Nigga!"
        }
        return JsonResponse(data)
    return redirect('home')


def land(request):
    if request.user.is_authenticated:
        return redirect('home')
    return render(request, 'registration/login.html')


# only4 testing
def test_func():
    return True
