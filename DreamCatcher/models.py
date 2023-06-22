from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models

# Create your models here.
class User(AbstractUser):
    groups = models.ManyToManyField(Group, related_name="dreamcatcher_users")
    user_permissions = models.ManyToManyField(Permission, related_name="dreamcatcher_users")

class Task(models.Model):
    user = models.ForeignKey(User, related_name="user_tasks",on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=800)
    datetime = models.DateTimeField()
    label = models.CharField(max_length=25)

    def __str__(self):
        return f"{self.user} : {self.name}"
