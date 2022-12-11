from django.db import models
from django.contrib.auth.models import AbstractUser
from ckeditor.fields import RichTextField


# Create your models here.


class Service(models.Model):
    service_title = models.CharField(max_length=200)
    about_service = models.TextField(null=True)
    avatar = models.ImageField(null=True, default="avatar.svg")

    def __str__(self):
        return self.service_title


class Team(models.Model):
    member_pic = models.ImageField(null=True, default="avatar.svg")
    member_name = models.CharField(max_length=200)
    member_position = models.CharField(max_length=200)
    about_member = models.TextField(null=True)

    def __str__(self):
        return self.member_name


class Activity(models.Model):
    activity_title = models.CharField(max_length=200)
    about_activity = models.TextField(null=True)
    activity_pic = models.ImageField(null=True, default="avatar.svg")
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-updated', '-created']

    def __str__(self):
        return self.activity_title


class Blog(models.Model):
    topic = models.CharField(max_length=200)
    writer = models.CharField(max_length=200)
    blog_pic = models.ImageField(null=True, default="avatar.svg")
    paragraph = RichTextField(blank=True, null=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-updated', '-created']

    def __str__(self):
        return self.topic

