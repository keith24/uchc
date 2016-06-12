from django.db import models
from mezzanine.pages.models import Page
from django_countries.fields import CountryField

class Club(Page):
	founded = models.DateField()
	city = models.CharField(max_length=50,default="")
	country = CountryField()
	website = models.URLField(default="")
	blurb = models.TextField(default="")
	img1 = models.ImageField(default="")
	img2 = models.ImageField(default="")
	img3 = models.ImageField(default="")
	img4 = models.ImageField(default="")
	img5 = models.ImageField(default="")

	class Meta:
		verbose_name = "Club"
		verbose_name_plural = "Clubs"
		ordering = ["founded"]

class ClubIndex(Page):
	class Meta:
		verbose_name = "Clubs Index"
		verbose_name_plural = "Clubs Indicies"
