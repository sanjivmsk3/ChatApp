from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class PostDetails(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='image/')
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class UserChat(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    massage = models.CharField(max_length=1000)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.massage