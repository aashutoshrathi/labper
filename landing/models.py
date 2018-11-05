
import datetime
import uuid
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
    class Meta:
        ordering = ('user',)
        verbose_name = 'Profile'
        verbose_name_plural = 'Profiles'

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.URLField(null=True, blank=True,
                             help_text='Profile picture URL')
    avatar_small = models.URLField(
        null=True, blank=True, help_text='Profile picture smaller URL')

    def __str__(self):
        return '%s %s' % (self.user.first_name, self.user.last_name)

    @property
    def roll_no(self):
        return self.user.email.split('@')[0]


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()


def current_year():
    return datetime.date.today().year


class Session(models.Model):
    class Meta:
        ordering = ('type',)
        verbose_name = 'Session'
        verbose_name_plural = 'Session'
        unique_together = ("type", "year")

    SESSION_CHOICES = (
        ('a', 'Autumn'),
        ('w', 'Winter'),
    )

    type = models.CharField(max_length=20, choices=SESSION_CHOICES)
    year = models.IntegerField(default=current_year, validators=[
        MinValueValidator(current_year()),
        MaxValueValidator(2100)
    ])

    def __str__(self):
        sessions = {'a': 'Autumn', 'w': 'Winter'}
        return sessions[self.type] + "-" + str(self.year)


class Course(models.Model):
    class Meta:
        ordering = ('name',)
        verbose_name = 'Course'
        verbose_name_plural = 'Courses'
        unique_together = ("code", "session")

    name = models.CharField(max_length=50)
    code = models.CharField(max_length=10, help_text="Unique Course Code")
    session = models.ForeignKey(Session, on_delete=models.CASCADE,
                                help_text="Session when this course is to be taught")
    target_batch = models.IntegerField(help_text="Year when target batch will graduate", default=2020, validators=[
        MinValueValidator(2019),
        MaxValueValidator(2104)])

    def __str__(self):
        return str(self.session) + " " + self.name


class Student(models.Model):
    class Meta:
        ordering = ('profile',)
        verbose_name = 'Student'
        verbose_name_plural = 'Students'

    BRANCH_CHOICES = (
        ('51', 'B.Tech CSE'),
        ('52', 'B.Tech IT'),
        ('61', 'M.Tech CSE'),
        ('62', 'M.Tech IT'),
        ('71', 'Ph.D.'),
    )

    profile = models.OneToOneField(
        Profile, on_delete=models.CASCADE, related_name='student_profile')
    batch = models.IntegerField()
    branch = models.CharField(max_length=50, choices=BRANCH_CHOICES)
    course = models.ManyToManyField(Course, related_name='student_course')

    def __str__(self):
        return self.profile.user.first_name

    @property
    def roll_no(self):
        return self.profile.user.email.split('@')[0]


class Teacher(models.Model):
    class Meta:
        ordering = ('profile',)
        verbose_name = 'Teacher'
        verbose_name_plural = 'Teachers'

    profile = models.OneToOneField(
        Profile, on_delete=models.CASCADE, related_name='teacher_profile')
    course = models.ManyToManyField(Course, related_name='teacher_course')

    def __str__(self):
        return str(self.profile)


class Assistant(models.Model):
    class Meta:
        ordering = ('profile',)
        verbose_name = 'assistant'
        verbose_name_plural = 'assistants'

    profile = models.OneToOneField(
        Profile, on_delete=models.CASCADE, related_name='assistant_profile')
    course = models.ManyToManyField(Course, related_name='assistant_course')

    def __str__(self):
        return self.profile.user.first_name

    @property
    def roll_no(self):
        return self.profile.user.email.split('@')[0]


class Lab(models.Model):
    class Meta:
        ordering = ('id',)
        verbose_name = 'Lab'
        verbose_name_plural = 'Labs'

    id = models.IntegerField(unique=True, primary_key=True)
    course = models.ForeignKey(
        Course, related_name='course', on_delete=models.CASCADE)
    date = models.DateField(help_text='Enter Date of Lab')
    start_time = models.TimeField()
    end_time = models.TimeField()
    description = models.CharField(
        max_length=256, help_text='Add brief Lab description', blank=True)

    def __str__(self):
        return self.course.name


class Submission(models.Model):
    class Meta:
        ordering = ('student',)
        verbose_name = 'Submission'
        verbose_name_plural = 'Submissions'

    id = models.IntegerField(unique=True, default=uuid.uuid4, primary_key=True)
    lab = models.ForeignKey(Lab, related_name='lab', on_delete=models.CASCADE)
    student = models.ForeignKey(
        Profile, related_name='student', on_delete=models.CASCADE)

    def __str__(self):
        return self.lab.name + self.student.user.first_name
