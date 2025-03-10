from django.db import models
from django.contrib.auth.models import User

class JoinUser(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    userID = models.CharField(max_length=40)
    

    def __str__(self):
        return self.user.username