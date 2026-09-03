from django.contrib import admin
# pyrefly: ignore [missing-import]
from .models import Post, Comment, Tag, UserProfile

admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Tag)
admin.site.register(UserProfile)
