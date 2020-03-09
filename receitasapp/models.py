from django.db import models
from datetime import datetime

class Receita(models.Model):
  name = models.CharField(max_length=200)
  ingredients = models.TextField()
  steps = models.TextField()
  time = models.IntegerField()
  category = models.CharField(max_length=100)
  creation_date = models.DateField(default=datetime.now())
