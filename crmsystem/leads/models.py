from django.db import models

class Lead(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=25)
    age = models.IntegerField()
