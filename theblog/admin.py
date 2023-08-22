from django.contrib import admin
from .models import Post, Category, Comment, Author, PostView
admin.site.register(Post)
admin.site.register(Category)
admin.site.register(Comment)
admin.site.register(Author)
admin.site.register(PostView)
