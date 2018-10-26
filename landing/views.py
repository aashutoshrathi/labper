from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import Profile, Teacher
from django.http import JsonResponse
from django.views import View
from .forms import AddCourse

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


class AddCourse(View):
    def get(self, request):
        if request.user.profile.teacher_profile:
            form = AddCourse()
            return render(request, 'landing/forms_default.html', {'form': form})
        else:
            messages.error(request, 'Not for you nigga!')
            return render(request, 'landing/home', {'form': form})

    def post(self, request):
        form = AddCourse(request.POST, request.user)
        if form.is_valid():
            form = AddCourse(request.POST)
            form.save()
            messages.success(request, 'Your course was successfully updated!')
            return redirect('home')
        else:
            messages.error(request, 'Course Code already in use.')
        return render(request, 'landing/forms_default.html', {'form': form})


def land(request):
    if request.user.is_authenticated:
        return redirect('home')
    return render(request, 'registration/login.html')


# only4 testing
def test_func():
    return True
