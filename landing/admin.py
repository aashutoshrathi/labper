from django.contrib import admin

from .models import Profile, Teacher, Course, Assistant, Lab, Submission, Session

admin.site.register(Profile)
admin.site.register(Teacher)
admin.site.register(Course)
admin.site.register(Assistant)
admin.site.register(Lab)
admin.site.register(Submission)
admin.site.register(Session)
