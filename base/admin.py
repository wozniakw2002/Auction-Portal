from django.contrib import admin

# Register your models here.

from .models import Auction, Comment, Category, User

admin.site.register(User)
admin.site.register(Auction)
admin.site.register(Comment)
admin.site.register(Category)
