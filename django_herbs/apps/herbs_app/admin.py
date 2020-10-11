from django.contrib import admin

# Register your models here.

from .models import Herb_article, Comment

admin.site.register(Herb_article) 
admin.site.register(Comment) 
