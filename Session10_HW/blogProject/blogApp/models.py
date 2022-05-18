from statistics import mode
from tkinter import CASCADE
from django.db import models

# Create your models here.
class Post(models.Model):
  title = models.CharField(max_length=50)
  content = models.TextField()
  view = models.IntegerField(default=0)

  def __str__(self):
    return self.title

class Comment(models.Model):
  post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comment_set')
  content = models.TextField()
  
  def __str__(self):
    return self.content
