from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    pass

class Agent(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=25)
    

class Lead(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=25)
    age = models.IntegerField()
    agent = models.ForeignKey("Agent", on_delete=models.CASCADE, null=True)


