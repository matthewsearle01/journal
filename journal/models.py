from django.db import models
from django.urls import reverse

# Create your models here.


class Journal(models.Model):
    title = models.CharField(max_length=255, blank=False)
    link = models.URLField(max_length=255)
    date_created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['date_created']

    def __str__(self):
        return self. title
