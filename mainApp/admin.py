from django.contrib import admin
from .models import Urls

class UrlsModel(admin.ModelAdmin):
	list_display = ('url', 'short_link', 'text', 'date' )

admin.site.register(Urls, UrlsModel)
