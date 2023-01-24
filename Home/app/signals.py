from django.contrib.auth import get_user_model
from .models import userProfile
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.contrib.auth.models import User

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    try: 
        if created:
            userProfile.objects.create(user=instance,name=f'{instance.first_name} {instance.last_name}')
    except Exception:
        instance.delete()

@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.userprofile.save()