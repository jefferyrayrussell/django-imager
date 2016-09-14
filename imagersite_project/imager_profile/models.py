from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save


class ImagerProfile(models.Models):
    # this line should link this model to djangos user model and delete the instance of this model
    # when the link django user moddle is deleted
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

    def user_string(self):
        """a visual representation that appropriately displays when using the Django shell"""
        user = User.objects.filter(user=self.user)
        string = "{} shoots {} with a {}".format(user.first_name, user.photography_type, user.camera_type)
        return string


@receiver(post_save, sender=User)
def init_new_ImagerProfile:
    """initialise a new instance of this class when a new instance of djangos user class is saved"""
    ImagerProfile()
