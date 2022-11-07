from django.db import models
from django.contrib.auth.models import User


class RememberedUsername(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    username = models.CharField(max_length=320)

    def __str__(self):
        return self.username


class Domain(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    domain = models.CharField(max_length=320)
    usernames = models.ManyToManyField(RememberedUsername, related_name='domains', blank=True)

    def __str__(self):
        return self.domain
