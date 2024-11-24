from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.dispatch import receiver
from travel_project.user_profile.models import UserProfile


UserModel = get_user_model()


@receiver(post_save, sender=UserModel)
def create_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)