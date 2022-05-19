from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):

  author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='post_set')
  title = models.CharField(max_length=50)
  content = models.TextField()
  view = models.IntegerField(default=0)

  def __str__(self):
    return self.title

class Comment(models.Model):
  post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comment_set')
  author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comment_set')
  content = models.TextField()
  
  def __str__(self):
    return self.content
