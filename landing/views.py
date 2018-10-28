import profile

from .forms import AddCourseForm
from .models import Course, Profile, Teacher
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import redirect, render
from django.views import View


@login_required
def home(request):
    x = request.user
    target = Profile.objects.get(user=x)
    if not target.user.username.isdigit():
        teacher = Teacher.objects.get(profile=target)
        courses = teacher.course.all()
        context = {
            'upgd': True,
            'courses': courses,
        }
    else:
        context = {
            'upgd': False
        }
    return render(request, 'landing/home.html', context=context)


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
        t_courses = Teacher.objects.get(profile=request.user.profile).course.all()
        return render(request, 'landing/course_list.html', {'courses':t_courses})


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


@login_required
def teach_course(request, course, teacher):
    if request.user.profile.teacher_profile:
        current = Teacher.objects.get(id=teacher)
        course_current = Course.objects.get(code=course)
        current.course.add(course_current)
    else:
        data = {
            'error': "Forbidden",
            'description': "Not for you Nigga!"
        }
        return JsonResponse(data)
    messages.success(request, 'Your course was added successfully!')
    return redirect('ListCourseView')


def land(request):
    if request.user.is_authenticated:
        return redirect('home')
    return render(request, 'registration/login.html')


# only4 testing
def test_func():
    return True
