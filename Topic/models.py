from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class Topic(models.Model):
    topic = models.CharField(max_length=100)
    published_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.topic


class Comment(models.Model):
    comment = models.CharField(max_length=100)
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    commented_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.comment
