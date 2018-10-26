from django.contrib import admin

from .models import Profile, Teacher, Course, Assistant, Lab, Submission

admin.site.register(Profile)
admin.site.register(Teacher)
admin.site.register(Course)
admin.site.register(Assistant)
admin.site.register(Lab)
admin.site.register(Submission)
