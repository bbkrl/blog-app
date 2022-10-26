from django.contrib import admin
from .models import Profile, BlogPost, Comment, User, Subscription


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'author', 'dateTime')
    list_filter = ('dateTime', 'title', 'author')
    search_fields = ('title', 'content')
    prepopulated_fields = {'slug': ('title',)}
    raw_id_fields = ('author',)
    # date_hierarchy = 'publish'
    # ordering = ['status', 'publish']


class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ('subscriber_user_id', 'subscription_user_id', 'created_at')


admin.site.register(BlogPost, PostAdmin)
admin.site.register(Profile)
admin.site.register(Comment)
admin.site.register(Subscription, SubscriptionAdmin)
