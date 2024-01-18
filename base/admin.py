from django.contrib import admin

# Register your models here.

from .models import Auction, Comment, Item, Category

admin.site.register(Auction)
admin.site.register(Comment)
admin.site.register(Item)
admin.site.register(Category)