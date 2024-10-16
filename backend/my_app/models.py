from django.db import models

class UserProfile(models.Model):
    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.username


class UserDetail(models.Model):
    profile = models.OneToOneField(UserProfile, on_delete=models.CASCADE)
    bio = models.TextField()

class UserGroup(models.Model):
    name = models.CharField(max_length=100)
    users = models.ManyToManyField(UserProfile)

    def __str__(self):
        return self.name
