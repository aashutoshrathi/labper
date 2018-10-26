import uuid
from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
    class Meta:
        ordering = ('user',)
        verbose_name = 'Profile'
        verbose_name_plural = 'Profiles'

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.URLField(null=True, blank=True, help_text='Profile picture URL')
    avatar_small = models.URLField(null=True, blank=True, help_text='Profile picture smaller URL')

    def __str__(self):
        return self.user.first_name

    def get_fullname(self):
        full_name = '%s %s' % (self.user.first_name, self.user.last_name)
        return full_name.strip()


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()


class Course(models.Model):
    class Meta:
        ordering = ('name',)
        verbose_name = 'Course'
        verbose_name_plural = 'Courses'

    name = models.CharField(max_length=20)
    code = models.CharField(max_length=10, primary_key=True)
    session = models.CharField(max_length=10)

    def __str__(self):
        return self.session + self.name

class Teacher(models.Model):
    class Meta:
        ordering = ('profile',)
        verbose_name = 'Teacher'
        verbose_name_plural = 'Teachers'

    profile = models.OneToOneField(Profile, on_delete=models.CASCADE, related_name='teacher_profile')
    course = models.ManyToManyField(Course, related_name='teacher_course')

    def __str__(self):
        return self.profile.user.first_name


class Assistant(models.Model):
    class Meta:
        ordering = ('profile',)
        verbose_name = 'assistant'
        verbose_name_plural = 'assistants'

    profile = models.OneToOneField(Profile, on_delete=models.CASCADE, related_name='assistant_profile')
    course = models.ManyToManyField(Course, related_name='assistant_course')

    def __str__(self):
        return self.profile.user.first_name


class Lab(models.Model):
    class Meta:
        ordering = ('id',)
        verbose_name = 'Lab'
        verbose_name_plural = 'Labs'

    id = models.IntegerField(unique=True, primary_key=True)
    course = models.ForeignKey(Course, related_name='course', on_delete=models.CASCADE)
    date = models.DateField(help_text='Enter Date of Lab')
    start_time = models.TimeField()
    end_time = models.TimeField()

    def __str__(self):
        return self.course.name


class Submission(models.Model):
    class Meta:
        ordering = ('student',)
        verbose_name = 'Submission'
        verbose_name_plural = 'Submissions'

    id = models.IntegerField(unique=True, default=uuid.uuid4, primary_key=True)
    lab = models.ForeignKey(Lab, related_name='lab', on_delete=models.CASCADE)
    student = models.ForeignKey(Profile, related_name='student', on_delete=models.CASCADE)

    def __str__(self):
        return self.lab.name + self.student.user.first_name
