""" Django data models for organizing startup company data"""

from django.db import models


class Tag(models.Model):
    """Labels to help categorize data"""

    name = models.CharField(
        max_length=31,
        unique=True,
    )
    slug = models.CharField(
        max_length=31,
        unique=True,
        help_text="A label for URL config."
    )

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name


class Startup(models.Model):
    """Data about a Startup company"""

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

    def __str__(self):
        return self.name


class NewsLink(models.Model):
    """Link to external sources about a Startup"""
    title = models.CharField(max_length=31)
    slug = models.CharField(max_length=31)
    pub_date = models.DateField("Date published")
    link = models.URLField(max_length=255)
    startup = models.ForeignKey(
        Startup, on_delete=models.CASCADE
    )

    def __str__(self):
        return f"{self.startup}: {self.title}"
