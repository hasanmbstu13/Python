
from datetime import date

from django.db import models

from organizer.models import Startup, Tag

class Post(models.Model):
    """Blog post; news article about startup"""

    title = models.CharField(max_length=63)
    slug = models.SlugField(
        max_length=63,
        help_text="A label for URL config",
        unique_for_month="pub_date",
    )
    text = models.TextField()
    pub_date = models.DateField(
        "Date published", default=date.today
    )
    tags = models.ManyToManyField(
        Tag, related_name="blog_posts"
    )
    startup = models.ManyToManyField(
        Startup, related_name="blog_posts"
    )


    def __str__(self):
        date_string = self.pub_date.strftime("%Y-%m-%d")
        return f"{self.title} on {date_string}"