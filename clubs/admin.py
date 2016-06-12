from django.contrib import admin
from mezzanine.pages.admin import PageAdmin
from .models import Club, ClubIndex

admin.site.register(Club, PageAdmin)
admin.site.register(ClubIndex, PageAdmin)
