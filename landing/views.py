import datetime
from builtins import object

from .forms import AddCourseForm
from .models import Course, Profile, Student, Teacher
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import send_mail
from django.http import JsonResponse
from django.shortcuts import redirect, render
from django.template.loader import render_to_string
from django.views import View
from urllib3 import request

from brutus import settings
from landing.models import Assistant, Session


@login_required
def home(request):
    x = request.user
    month = datetime.date.today().month
    year = datetime.date.today().year
    s_type = 'w'
    if month > 6:
        s_type = 'a'
    session, create = Session.objects.get_or_create(year=year, type=s_type)
    target = Profile.objects.get(user=x)
    if not target.user.username.isdigit():
        teacher, create = Teacher.objects.get_or_create(profile=target)
        courses = teacher.course.all()
        context = {
            'upgd': True,
            'courses': courses,
            'session': session,
        }
    else:
        batch = int(target.roll_no[:4]) + 4
        branch = target.roll_no[4:6]
        student, create = Student.objects.get_or_create(
            profile=target, batch=batch, branch=branch)
        xcourses = Course.objects.filter(target_batch=batch)
        for c in xcourses:
            student.course.add(c)
        courses = student.course.all()
        context = {
            'student': student,
            'courses': courses,
            'upgd': False,
            'session': session,
        }
    return render(request, 'landing/home.html', context=context)


class ListCourseView(View):
    def get(self, request):
        t_courses = Teacher.objects.get(
            profile=request.user.profile).course.all()
        other = Course.objects.all()
        other_course = []
        for c in other:
            if c not in t_courses:
                other_course.append(c)
        return render(request, 'landing/course_list.html', {'courses': t_courses,
                                                            'other_courses': other_course})


class AddCourseView(View):
    def get(self, request):
        try:
            if request.user.profile.teacher_profile or request.user.is_superuser:
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
            tform = form.save(commit=False)
            tform.save()
            current_site = get_current_site(request)
            code = tform.code
            subject = 'Invitation to ' + \
                str(tform.name) + ' by ' + str(request.user.profile)
            org_email = settings.EMAIL_HOST_USER
            students = Student.objects.filter(batch=tform.target_batch)
            instructor = request.user.profile
            for student in students:
                message = render_to_string('registration/account_activation_email.html', {
                    'student': student,
                    'course': tform.name,
                    'domain': current_site,
                    'teacher': instructor
                })
                student.profile.user.email_user(subject, message)
                send_mail(subject, message, org_email, [
                          student.profile.user.email], fail_silently=True)
            messages.success(
                request, 'Your course was added successfully and email has been sent.')
            return redirect('home')
        else:
            messages.error(request, 'Course Code already in use.')
        return render(request, 'landing/forms_default.html', {'form': form,
                                                              'form_title': title})


@login_required
def teach_course(request, course, teacher, session):
    if request.user.profile.teacher_profile:
        current = Teacher.objects.get(id=teacher)
        course_current = Course.objects.get(code=course, session__id=session)
        current.course.add(course_current)
    else:
        data = {
            'error': "Forbidden",
            'description': "Not for you Nigga!"
        }
        return JsonResponse(data)
    messages.success(request, 'Your course was added successfully!')
    return redirect('course_detail', course, session)


@login_required
def leave_course(request, course, session, teacher):
    if request.user.profile.teacher_profile:
        current = Teacher.objects.get(id=teacher)
        course_current = Course.objects.get(code=course, session__id=session)
        current.course.remove(course_current)
    else:
        data = {
            'error': "Forbidden",
            'description': "Not for you Nigga!"
        }
        return JsonResponse(data)
    messages.success(request, 'Your have left the course successfully!')
    return redirect('list_course')


@login_required
def course_detail(request, course, session):
    if request.user.profile:
        course = Course.objects.get(code=course, session__id=session)
        teachers = Teacher.objects.filter(course=course)
        students = Student.objects.filter(batch=course.target_batch)
        assistants = Assistant.objects.filter()
        context = {
            'course': course,
            'page_title': course.code,
            'teachers': teachers,
            'students': students,
        }
        return render(request, 'landing/course_detail.html', context=context)
    messages.error(request, 'Sorry, your sourcery do not work here :)')
    return redirect('home')


def land(request):
    if request.user.is_authenticated:
        return redirect('home')
    return render(request, 'registration/login.html')


def about(request):
    return render(request, 'landing/about_us.html')


def ide(request):
    return render(request, 'landing/ide.html')


# only4 testing
def test_func():
    return True
