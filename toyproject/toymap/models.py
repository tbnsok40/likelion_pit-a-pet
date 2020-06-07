from django.db import models

# Create your models here.

class addr(models.Model):
    body = models.CharField(max_length=30)

    def __str__(self):
         return self.body