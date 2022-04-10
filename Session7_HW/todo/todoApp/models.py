from django.db import models

# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length=500)
    detail = models.TextField()
    date = models.DateField()
    date_str = models.CharField(max_length=20)

    def __str__(self):
        return self.title

