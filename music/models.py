from django.db import models
from django.contrib.auth import get_user_model

class Music(models.Model):
  seller = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
  name = models.CharField(max_length=64)
  instrument = models.CharField(max_length=24)
  description = models.TextField()
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  def __str__(self):
    return self.name