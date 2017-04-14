from modeltranslation.translator import translator, TranslationOptions

from .models import HomePage


class TranslatedHomePage(TranslationOptions):
    fields = ('content',)

translator.register(HomePage, TranslatedHomePage)
