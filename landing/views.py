from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Profile, Teacher, Course
from django.http import JsonResponse
from django.views import View
from .forms import AddCourseForm

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


class ListCourseView(View):
    def get(self, request):
        courses = Course.objects.all()
        return render(request, 'landing/course_list.html', {'courses':courses})


class AddCourseView(View):
    def get(self, request):
        try:
            if request.user.profile.teacher_profile:
                form = AddCourseForm()
                title = "Add Course"
                return render(request, 'landing/forms_default.html', {'form': form, 
                                                                      'form_title': title})
        except:
            messages.error(request, 'Permission Denied!')
            return render(request, 'landing/home.html')

    def post(self, request):
        form = AddCourseForm(request.POST, request.user)
        title = "Add Course"
        if form.is_valid():
            form = AddCourseForm(request.POST)
            form.save()
            messages.success(request, 'Your course was added successfully!')
            return redirect('home')
        else:
            messages.error(request, 'Course Code already in use.')
        return render(request, 'landing/forms_default.html', {'form': form, 
                                                              'form_title': title})


def land(request):
    if request.user.is_authenticated:
        return redirect('home')
    return render(request, 'registration/login.html')


# only4 testing
def test_func():
    return True
