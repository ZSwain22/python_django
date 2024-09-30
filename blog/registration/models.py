from django.db import models

# Create your models here.
class UserInfo(models.Model):
    firstName = models.CharField(max_length = 100)
    lastName = models.CharField(max_length = 100)
    username = models.CharField(max_length = 100)
    password = models.CharField(max_length = 100)
    
    def __str__(self):
        return self.username