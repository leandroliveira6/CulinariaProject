from django.db import models


class Pessoa(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)

    def __str__(self):
        return '{}'.format(self.name)
