"""Creates the user profile of a simple Django image management website."""

from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class ImagerProfile(models.Model):
    """Create a class of objects that serve as the Imager Profile model."""

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    camera_type = models.CharField('camera type', blank=True)
    address = models.CharField('address', blank=True)
    website = models.URLField('website', blank=True)
    photography_type = models.CharField('photography type', blank=True)
    facebook = models.URLField('facebook', blank=True)

    def active():
        """Filter the active users as indicated in the User Profile."""
        users = User.objects.filter(is_active=True)
        return users.ImagerProfile

    def user_string(self):
        """Provide a visual representation of the model."""
        string = "{} shoots {} with a {}".format(self.user.first_name,
                                                 self.user.photography_type,
                                                 self.user.camera_type)
        return string


@receiver(post_save, sender=User)
def init_new_imager_profile(sender, instance):
    """Initialise a new instance of Imager Profile."""
    pro1 = ImagerProfile(instance)
    pro1.save()
