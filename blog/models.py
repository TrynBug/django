from django.conf import settings
from django.db import models
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

class PyTest(models.Model):

    created_date = models.DateTimeField(default=timezone.now)
    count = models.IntegerField()
    text = models.TextField()
    word1 = models.CharField(max_length=1000)
    word2 = models.CharField(max_length=1000)
    word3 = models.CharField(max_length=1000)

    def publish(self):
        self.save()

    def __str__(self):
        return self.text

# python manage.py makemigrations blog
# python manage.py migrate blog