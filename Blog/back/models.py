from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils.timezone import now
from taggit.managers import TaggableManager
from django.shortcuts import render, redirect, get_object_or_404


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True)
    image = models.ImageField(upload_to="profile_pics", blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    phone_no = models.IntegerField(blank=True, null=True)
    facebook = models.CharField(max_length=300, blank=True, null=True)
    instagram = models.CharField(max_length=300, blank=True, null=True)
    linkedin = models.CharField(max_length=300, blank=True, null=True)

    def __str__(self):
        return str(self.user)


class BlogPost(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    slug = models.SlugField(max_length=130)
    content = models.TextField()
    image = models.ImageField(upload_to="profile_pics", blank=True, null=True)
    dateTime = models.DateTimeField(auto_now_add=True)

    tags = TaggableManager()

    def __str__(self):
        return str(self.author) + " Blog Title: " + self.title

    def get_absolute_url(self):
        return reverse('blogs')


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    blog = models.ForeignKey(BlogPost, on_delete=models.CASCADE)
    parent_comment = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)
    dateTime = models.DateTimeField(default=now)

    def __str__(self):
        return self.user.username + " Comment: " + self.content


class Subscription(models.Model):
    subscriber_user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='subscriptions')
    subscription_user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='subscribers')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.subscriber_user_id} is subscribe on {self.subscription_user_id}'

    def show_subscriptions(self, subscriber_user_id):
        user = get_object_or_404(User, id=subscriber_user_id)
        subscription = user.subscriptions.all()
        # context = {
        #     'user': user,
        #     'subscription': subscription,
        # }
        return subscription
