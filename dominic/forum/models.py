from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Category(models.Model):
    name = models.CharField(
        max_length=100, help_text="depression, substance Use, schizophreria, bipolar, others")
    dateadded = models.DateTimeField(auto_now_add=True)
    datemodified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.name)


class Article(models.Model):
    author = models.ForeignKey(
        User, related_name="post_author", blank=True, null=True, on_delete=models.SET_NULL)
    title = models.CharField(max_length=100, blank=True, null=True)
    category = models.ForeignKey(
        Category, related_name="post_category", blank=True, null=True, on_delete=models.SET_NULL)
    text = models.TextField()
    dateadded = models.DateTimeField(auto_now_add=True)
    datemodified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.title)
