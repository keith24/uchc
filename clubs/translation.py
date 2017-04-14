from modeltranslation.translator import translator, TranslationOptions
from django.utils.translation import ugettext_lazy as _, ugettext

from .models import Club, ClubIndex


class TranslatedClub(TranslationOptions):
	fields = ('city', 'blurb', )

class TranslatedClubIndex(TranslationOptions):
	fields = ()

translator.register(Club, TranslatedClub)
translator.register(ClubIndex, TranslatedClubIndex)
