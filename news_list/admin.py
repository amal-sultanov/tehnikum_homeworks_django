from django.contrib import admin

from .models import NewsCategory, News, Wishlist

admin.site.register(NewsCategory)
admin.site.register(News)
admin.site.register(Wishlist)
