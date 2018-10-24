from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import Profile
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
    x = request.user
    target = Profile.objects.get(user=x)
    if not target.user.username.isdigit():
        target.teacher = True
        target.save()
    else:
        data = {
            'error': "Forbidden",
            'description': "Not for you Nigga!"
        }
        return JsonResponse(data)
    return redirect('home')


@login_required
def downgrade(request):
    x = request.user
    target = Profile.objects.get(user=x)
    target.teacher = False
    target.save()
    return redirect('home')


def land(request):
    if request.user.is_authenticated:
        return redirect('home')
    return render(request, 'registration/login.html')


# only4 testing
def test_func():
    return True
