from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save


class ImagerProfile(models.Models):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    camera_type = models.CharField('camera type', blank=True)
    address = models.CharField('address', blank=True)
    website = models.URLField('website', blank=True)
    photography_type = models.CharField('photography type', blank=True)
    facebook = models.URLField('facebook', blank=True)

    def active():
        """make a database query for ImagerProfile's that are active in their User moddles"""
        users = User.objects.filter(is_active=True)
        return users.ImagerProfile


@receiver(post_save, sender=User)
    def init_new_ImagerProfile:
        ImagerProfile()

