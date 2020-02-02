"""Forms for the Organizer app"""

from django.core.exceptions import ValidationError
from django.forms import ModelForm

from .models import Tag

class SlugCleanMixin:
	"""Mixin class to ensure slug field is not create"""

	def clean_slug(self):
		"""Enusre slug is not 'create'

		This is an oversimplification!!! See the following link for how to raise the error correctly. 

		https://docs.djangoproject.com/en/3.0/ref/forms/validation/#raising-validation-error

		"""
		slug = self.cleaned_data["slug"]
		if slug == "create":
			raise ValidationError(
				"Slug may not be 'create'."
			)
		return slug

class TagForm(Form):
	"""HTML form for Tag objects"""

	name = CharField(max_length=31)
	slug = SlugField(
		help_text="A label for URL config",
		max_length=31,
		required=False,
	)

	def clean_name(self):
		"""Ensure Tag name is always lowercase"""
		return self.cleaned_data["name"].lower()

	

	def save(self):
		"""Save the data in the bound form"""
		return Tag.objects.create(
			name=self.cleaned_data["name"],
			slug=self.cleaned_data["slug"]
		)