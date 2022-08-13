from django.db import models

# Create your models here.

class Africa(models.Model):
    country = models.CharField(max_length = 30)
    capital = models.CharField(max_length = 30)

    def __str__(self):

        return self.country
