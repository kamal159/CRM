from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    phone_number = models.CharField(max_length=15, null=True, blank=True)

    def __str__(self):
        return self.username
    

class Lead(models.Model):
    SOURCE_CHOICES = (
        ("Youtube", "Youtube"), 
        ("Zoom", "Zoom"), 
        ("Facebook", "Facebook"),
    )

    first_name = models.CharField(max_length=20, default='')
    last_name = models.CharField(max_length=20, default='')
    age = models.IntegerField(default=0)

    phoned = models.BooleanField(default=False)
    source = models.CharField(choices=SOURCE_CHOICES, max_length=100, default='')

    profile_picture = models.ImageField(blank=True, null=True)
    special_files = models.FileField(blank=True, null=True)

    agent = models.ForeignKey("Agent", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
        

class Agent(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.user.email