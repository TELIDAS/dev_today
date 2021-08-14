from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from datetime import datetime, date


class Post(models.Model):
    title = models.CharField(max_length=250)
    title_tag = models.CharField(max_length=250, default='Blog Post')
    body = models.TextField()
    link = models.URLField()
    creation_date = models.DateField(auto_now_add=True)
    author = models.ForeignKey(User,
                               on_delete=models.CASCADE,
                               related_name='author')
    votes = models.ManyToManyField(User, related_name='blogpost')

    def __str__(self):
        return self.title

    def total_votes(self):
        return self.votes.count()

    def get_absolute_url(self):
        return reverse('post-detail', args=(str(self.id)))


class Comment(models.Model):
    post = models.ForeignKey(Post,
                             on_delete=models.CASCADE,
                             related_name='post_comment')
    author_name = models.ForeignKey(User,
                                    on_delete=models.CASCADE,
                                    related_name='comments_author')
    body = models.TextField()
    creation_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return '%s - %s' % (self.post.title, self.author_name)
