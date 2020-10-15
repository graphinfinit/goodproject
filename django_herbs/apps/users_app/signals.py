

from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


'''Определим метод postsave чтобы при создании пользователя он был неактивным'''
@receiver(post_save, sender=User)
def default_to_non_active(sender, instance, created, **kwargs):
    if not sender.is_superuser:
        if created:
            instance.is_active = False
            instance.save()
    else:
        pass