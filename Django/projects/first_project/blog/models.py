from django.db import models

from organizer.models import Startup, Tag

class Post(models.Model):
    title = models.CharField(max_length=63)
    slug = models.SlugField(max_length=63)
    text = models.TextField()
    pub_date = models.DateField()
    tags = models.ManyToManyField(Tag)
    startup = models.ManyToManyField(Startup)