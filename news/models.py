from django.db import models

# Create your models here.

class Headline(models.Model):
  title = models.CharField(max_length=200)
  para = models.TextField()
  url = models.TextField()
  

  def __str__(self):
    return self.title
