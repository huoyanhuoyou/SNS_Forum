from django.contrib import admin

# Register your models here.
from bbs.models import Plate, Article, Comment

admin.site.register(Plate)
admin.site.register(Article)
admin.site.register(Comment)

