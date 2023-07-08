from django.contrib import admin
from .models import Topic, Entry, BlogPost

admin.site.register(Topic)
admin.site.register(Entry)
admin.site.register(BlogPost)
