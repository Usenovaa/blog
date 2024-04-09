from django.contrib import admin
from .models import Post, Comment

admin.site.register(Post)


# class PostAdmin(admin.ModelAdmin):
#     list_display = ['title', 'author']
#     list_filter = ['category', 'author']
#     search_fields = ['title', 'body', 'tags__title']


# class CommentInline(admin.TabularInline):
#     model = Comment


# class PostAdmin(admin.ModelAdmin):
#     inlines = [CommentInline]
    


# admin.site.register(Post, PostAdmin)