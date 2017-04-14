from django.db import models

from mezzanine.pages.models import Page
from mezzanine.core.models import RichText

class HomePage(Page, RichText):
	"""
	This is the model used for the About page and nothing else.  Contains the about information as well as recent news stories
	"""

	class Meta:
		verbose_name = "Homepage"
		verbose_name_plural = "Homepages"
