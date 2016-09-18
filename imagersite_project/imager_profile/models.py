from __future__ import unicode_literals
from django.db import models
from django.dispatch import receiver
from django.contrib.auth.models import User
from django.db.models.signals import post_save
import uuid


class ImagerProfile(models.Model):
    # links this model to djangos user model and delete the instance of this model
    # when the link django user moddle is deleted
    profile_id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    camera_type = models.CharField('camera type', max_length=128, blank=True)
    address = models.CharField('address', max_length=128, blank=True)
    website = models.URLField('website', blank=True)
    photography_type = models.CharField('photography type', max_length=128, blank=True)
    facebook = models.URLField('facebook', blank=True)

    @classmethod
    def active_users(cls):
        '''make a bd query for ImagerProfile's that are active in their User models'''
        active_users = cls.objects.filter(user__is_active__exact=True)
        return active_users

    @property
    def is_active(self):
        '''Tells us if the current user is active'''
        return self.user.is_active

    def __str__(self):
        '''visual representation that displays when using the Django shell'''
        user = User.objects.filter(user=self.user)
        string = "{} shoots {} with a {}".format(user.first_name,
                                                 user.photography_type,
                                                 user.camera_type)
        return string


@receiver(models.signals.post_save, sender=User)
def init_new_imager_profile(sender, **kwargs):
    '''initialise new instance of this class when a new instance of user class is saved'''
    ImagerProfile(user=kwargs['instance']).save()
