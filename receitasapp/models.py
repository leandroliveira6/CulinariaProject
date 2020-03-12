from django.db import models
from datetime import datetime
from django.utils import timezone

from django.contrib.auth.models import User

class Receita(models.Model):
  name = models.CharField(max_length=200)
  ingredients = models.TextField()
  steps = models.TextField()
  time = models.IntegerField()
  category = models.CharField(max_length=100)
  creation_date = models.DateField(auto_now=True, blank=True)
  owner_user = models.ForeignKey(User, on_delete=models.CASCADE)
  visible = models.BooleanField(default=False)
  picture = models.ImageField(upload_to='pictures/%d/%m/%Y', blank=True)

  def __str__(self):
    return '{}'.format(self.name)
