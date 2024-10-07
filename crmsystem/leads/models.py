from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    pass

class Agent(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.user.username


class Lead(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=25)
    age = models.IntegerField()
    description = models.TextField(default='This Lead was created before description was required', blank=False, null=False)
    agent = models.ForeignKey("Agent", on_delete=models.CASCADE, null=True)

    def __str__(self) -> str:
        return self.first_name + " " + self.last_name

