from django.db import models
from django.urls import reverse, reverse_lazy


# Create your models here.

class User(models.Model):
    userName = models.CharField(max_length=255)
    age = models.IntegerField()


class Post(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now=True)
    # user = models.ForeignKey('User', on_delete=models.CASCADE)
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE, related_name='author')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("post_detail", args=[str(self.id)])
