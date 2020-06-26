from django.conf import settings
from django.db import models
from django.utils import timezone


class Morpheme(models.Model):
    created_date = models.DateTimeField(default=timezone.now)
    updated_date = models.DateTimeField(blank=True, null=True)
    text = models.TextField()
    words = models.TextField()

    def publish(self):
        self.save()

    def __str__(self):
        return self.text