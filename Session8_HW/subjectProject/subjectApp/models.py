from django.db import models

# Create your models here.
class Major(models.Model):
    name = models.CharField(max_length=500)
    
    def __str__(self):
        return self.name

class Subject(models.Model):
    major = models.ForeignKey('Major', on_delete=models.CASCADE, related_name='subject')
    subject_name = models.CharField(max_length=500)
    prof_name = models.CharField(max_length=100)
    memo = models.CharField(max_length=1000)

    def __str__(self):
        return self.subject_name