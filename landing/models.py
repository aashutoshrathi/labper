from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
    class Meta:
        ordering = ('user',)
        verbose_name = 'Profile'
        verbose_name_plural = 'Profiles'

    GENDER_CHOICES = (
        ('m', 'Male'),
        ('f', 'Female'),
        ('o', 'Other'),
        ('n', 'Not Specified')
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.URLField(null=True, blank=True, help_text='Profile picture URL')
    avatar_small = models.URLField(null=True, blank=True, help_text='Profile picture smaller URL')
    teacher = models.BooleanField(default=False)

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
