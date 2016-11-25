from django.db import models
from django.core.urlresolvers import reverse
from django.db.models.signals import pre_save
from django.utils.text import slugify

# Create your models here.
class Post(models.Model):
    '''Models for Posts'''
    title = models.CharField(max_length=100)
    image = models.FileField(null=True, blank=True)
    slug = models.SlugField(unique=True)
    content = models.TextField()
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __str__(self):
        return '{0}: {1}...'.format(self.title, self.content[:20])

    def get_absolute_url(self):
        return reverse("posts:detail", kwargs={"id": self.id})
        # return '/posts/{0}/'.format(self.id)

def pre_save_post_reciever(sender, instance, *args, **kwargs):
    slug = slugify(instance.title)
    exists = Post.objects.filter(slug=slug).exists()
    if exists:
        slug = "{0}-{1}".format(slugify(instance.title), instance.id)
    instance.slug = slug
    
pre_save.connect(pre_save_post_reciever, sender= Post) 