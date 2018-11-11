from django.db import models
from pytz import timezone


def user_directory_path(instance, filename):
    return '{0}/{1}'.format(instance.timestamp, filename)


class TestCase(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    code_file = models.FileField(upload_to=user_directory_path)
