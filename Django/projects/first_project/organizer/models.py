from django.db import models


class Tag(models.Model):
    name = models.CharField(
        max_length=31,
        unique=True,
    )
    slug = models.CharField(
        max_length=31,
        unique=True,
        help_text="A label for URL config."
    )

class Startup(models.Model):
    name = models.CharField(
        max_length=31,
        db_index=True,
    )
    slug = models.SlugField(
        max_length=31,
        unique=True,
        help_text="A label for URL config."
    )
    description = models.TextField()
    founded_date = models.DateField("Date founded")
    contact = models.EmailField()
    website = models.URLField(max_length=255)
    tags = models.ManyToManyField(Tag)

class NewsLink(models.Model):
    title = models.CharField(max_length=31)
    slug = models.CharField(max_length=31)
    pub_date = models.DateField("Date published")
    link = models.URLField(max_length=255)
    startup = models.ForeignKey(
        Startup, on_delete=models.CASCADE
    )
