from django.db import models
from django.contrib.auth.models import User

class Poll(models.Model):
    question = models.CharField(max_length=255)
    created_by = models.ForeignKey(User, related_name='polls', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

class Option(models.Model):
    poll = models.ForeignKey(Poll, related_name='options', on_delete=models.CASCADE)
    text = models.CharField(max_length=255)

class Vote(models.Model):
    poll = models.ForeignKey(Poll, related_name='votes', on_delete=models.CASCADE)
    option = models.ForeignKey(Option, related_name='votes', on_delete=models.CASCADE)
    voted_by = models.ForeignKey(User, related_name='votes', on_delete=models.CASCADE)
    voted_at = models.DateTimeField(auto_now_add=True)

class Comment(models.Model):
    poll = models.ForeignKey(Poll, related_name='comments', on_delete=models.CASCADE)
    text = models.TextField()
    created_by = models.ForeignKey(User, related_name='comments', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    parent = models.ForeignKey('self', null=True, blank=True, related_name='replies', on_delete=models.CASCADE)


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture = models.ImageField(upload_to='profile_pics/', null=True, blank=True)