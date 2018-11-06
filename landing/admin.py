from .models import Assistant, Course, Lab, Profile, Session, Submission, \
    Teacher
from django.contrib import admin

from landing.models import Problem, Student


admin.site.register(Profile)
admin.site.register(Teacher)
admin.site.register(Course)
admin.site.register(Assistant)
admin.site.register(Lab)
admin.site.register(Submission)
admin.site.register(Session)
admin.site.register(Student)
admin.site.register(Problem)
