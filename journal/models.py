from distutils.fancy_getopt import FancyGetopt
from django.db import models
from taggit.managers import TaggableManager

# Create your models here.


class Journal(models.Model):
    title = models.CharField(max_length=255, blank=False)
    link = models.URLField(max_length=255)
    date_created = models.DateTimeField(auto_now_add=True)
    tags = TaggableManager(help_text="")
    document = models.FileField(
        upload_to='documents/', null=True, blank=True)


class Meta:
    ordering = ['date_created']


def __str__(self):
    return self. title
