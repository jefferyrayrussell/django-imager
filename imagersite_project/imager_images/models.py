# Imager_images model

from __future__ import unicode_literals
from django.db import models
from django.dispatch import receiver
from django.contrib.auth.models import User
from django.db.models.signals import post_save
import uuid


class Photo(models.Model):
"""Photos submitted by user."""
    photo_id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    albums = models.ManyToManyField('Album')
    file = models.ImageField(upload_to=user_directory_path)
    date_uploaded = models.DateTimeField('date uploaded', blank=True)
    date_modified = models.DateTimeField('date modified', blank=True)
    date_published = models.DateTimeField('date published', blank=True)
    published = models.CharField(max_length=128,
                                choices=[('private', 'private'),
                                        ('shared', 'shared'),
                                        ('public', 'public')])


class Album(models.Model):
"""Albums submitted by user."""
    photo_id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    photos = models.ManyToManyField('Photos')
    cover = models.ForeignKey(Photo)
    title = models.CharField("title", max_length=128, blank=True)
    description = models.CharField("description", max_length=128, blank=True)
    date_created = models.DateTimeField('date created', blank=True)
    date_modified = models.DateTimeField('date modified', blank=True)
    date_published = models.DateTimeField('date published', blank=True)
    published = models.CharField(max_length=128,
                                choices=[('private', 'private'),
                                        ('shared', 'shared'),
                                        ('public', 'public')])