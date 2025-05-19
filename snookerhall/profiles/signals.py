from django.contrib.auth.signals import user_logged_in
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import UserProfile


@receiver(user_logged_in)
def ensure_profile_exists(sender, user, request, **kwargs):
    UserProfile.objects.get_or_create(user=user)
