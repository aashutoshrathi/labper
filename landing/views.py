import datetime
from builtins import object

from .forms import AddCourseForm, AddLabForm
from .models import Course, Profile, Student, Teacher, Lab
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import send_mail
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import redirect, render
from django.template.loader import render_to_string
from django.views import View
from urllib3 import request

from brutus import settings
from landing.forms import AddAssistantForm, AddStudentForm, EditCourseForm
from landing.models import Assistant, Session


@login_required
def home(request):
    x = request.user
    # print(x.last_login)
    # print(x.date_joined)
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
                button = "Submit Course"
                return render(request, 'landing/forms_default.html', {'form': form,
                                                                      'button': button,
                                                                      'form_title': title})
        except:
            messages.error(request, 'Permission Denied!')
            return render(request, 'landing/home.html')

    def post(self, request):
        form = AddCourseForm(request.POST, request.user)
        title = "Add Course"
        button = "Update Course"
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
            return redirect('list_course')
        else:
            messages.error(request, 'Course Code already in use.')
        return render(request, 'landing/forms_default.html', {'form': form, 'button': button,
                                                              'form_title': title})


class EditCourseView(View):
    def get(self, request, course, session):
        try:
            if request.user.profile.teacher_profile or request.user.is_superuser:
                xcourse = Course.objects.get(
                    code=course, session__id=session)
                form = EditCourseForm(instance=xcourse)
                title = "Edit Course"
                button = "Update Course"
                return render(request, 'landing/forms_default.html', {'form': form,
                                                                      'button': button,
                                                                      'form_title': title})
        except:
            messages.error(request, 'Permission Denied!')
            return render(request, 'landing/home.html')

    def post(self, request, course, session):
        xcourse = Course.objects.get(code=course, session__id=session)
        form = EditCourseForm(request.POST, instance=xcourse)
        title = "Edit Course"
        button = "Update Course"
        if form.is_valid():
            form.save()
            messages.success(request, 'Your course: ' +
                             str(xcourse.name) + ' has been updated successfully!')
            return redirect('home')
        else:
            messages.error(request, 'Course Code already in use.')
        return render(request, 'landing/forms_default.html', {'form': form,
                                                              'button': button,
                                                              'form_title': title})


class AddLabView(View):
    def get(self, request, course, session):
        if request.user.profile.teacher_profile or request.user.is_superuser:
            form = AddLabForm(request.POST)
            title = "Add Lab"
            button = "Submit Lab"
            return render(request, 'landing/forms_default.html', {'form': form,
                                                                  'button': button,
                                                                  'form_title': title})

    def post(self, request, course, session):
        form = AddLabForm(request.POST, request.user)
        title = "Add Lab"
        button = "Update Lab"
        if form.is_valid():
            form = AddLabForm(request.POST)
            tform = form.save(commit=False)
            tform.course = Course.objects.get(code=course, session_id=session)
            tform.save()
            messages.success(
                request, 'Your lab was added successfully!')
            return redirect('home')
        else:
            messages.error(request, 'Lab Code already in use.')
        return render(request, 'landing/forms_default.html', {'form': form, 'button': button,
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
        students = Student.objects.filter(course=course)
        assistants = Assistant.objects.filter(course=course)
        labs = Lab.objects.filter(course=course)
        s_form = AddStudentForm(request.POST)
        a_form = AddAssistantForm(request.POST)
        if s_form.is_valid():
            rn = s_form.cleaned_data['roll_no']
            student = None
            all_student = Student.objects.all()
            for s in all_student:
                if s.roll_no == rn:
                    student = s
            if student is None:
                messages.error(request, "No such student exist in DB")
            if course in student.course.all():
                messages.warning(
                    request, "User already enrolled for the course -_-")
            else:
                student.course.add(course)
                messages.success(request, "Added " +
                                 str(student) + " successfully!")

        if a_form.is_valid():
            rn = a_form.cleaned_data['roll_no']
            ta = None
            student = None
            all_student = Student.objects.all()
            for s in all_student:
                if s.roll_no == rn:
                    student = s
            ta, create = Assistant.objects.get_or_create(
                profile = student.profile)
            if course in ta.course.all():
                messages.warning(
                    request, "Assistant already assigned for this course -_-")
            else:
                ta.course.add(course)
                messages.success(request, "Added " +
                                 str(ta) + " as TA successfully!")

        context = {
            'course': course,
            's_form': s_form,
            'labs': labs,
            'a_form': a_form,
            'page_title': course.code,
            'teachers': teachers,
            'students': students,
            'assistants': assistants,
        }
        return render(request, 'landing/course_detail.html', context=context)
    messages.error(request, 'Sorry, your sourcery do not work here :)')
    return redirect('home')


@login_required()
def remove_student(request, course, student, session):
    student = Student.objects.get(id=student)
    course = Course.objects.get(code=course, session__id=session)
    student.course.remove(course)
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))


@login_required()
def remove_assistant(request, course, assistant, session):
    assistant = Assistant.objects.get(id=assistant)
    course = Course.objects.get(code=course, session__id=session)
    assistant.course.remove(course)
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))


def land(request):
    if request.user.is_authenticated:
        return redirect('home')
    return render(request, 'registration/login.html')


def about(request):
    return render(request, 'landing/about_us.html')


def ide(request):
    return render(request, 'landing/ide.html')


def test_func():
    return True
