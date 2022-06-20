from django.contrib import admin
from .models import Profile, BlogPost, Comment, User


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'author', 'dateTime')
    list_filter = ('dateTime', 'title', 'author')
    search_fields = ('title', 'content')
    prepopulated_fields = {'slug': ('title',)}
    raw_id_fields = ('author',)
    # date_hierarchy = 'publish'
    # ordering = ['status', 'publish']


admin.site.register(BlogPost, PostAdmin)
admin.site.register(Profile)
admin.site.register(Comment)
