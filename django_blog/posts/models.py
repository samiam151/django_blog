from django.db import models
from django.core.urlresolvers import reverse

# Create your models here.
class Post(models.Model):
    '''Models for Posts'''
    title = models.CharField(max_length=100)
    content = models.TextField()
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __str__(self):
        return '{0}: {1}...'.format(self.title, self.content[:20])

    def get_absolute_url(self):
        return reverse("posts:detail", kwargs={"id": self.id})
        # return '/posts/{0}/'.format(self.id)
