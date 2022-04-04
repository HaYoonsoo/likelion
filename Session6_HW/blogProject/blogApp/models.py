from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=200)
    category = models.CharField(max_length=100, default='')
    content = models.TextField()
    create_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title