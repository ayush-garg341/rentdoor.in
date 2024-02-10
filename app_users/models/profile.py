"""Extending Django user module."""

from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
    """This model is to save some extra fields not supported by original user model."""

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_pic = models.TextField(blank=True, null=True)
    profile_pic_link = models.CharField(max_length=512, blank=True, null=True)
    job_title = models.CharField(max_length=500, blank=True, null=True)

    class Meta:
        """Table Name in mysql."""

        db_table = "profile"


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs) -> None:
    """Create profile when user is created with 1-to-1 mapping."""
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    """Save profile in db."""
    instance.profile.save()
