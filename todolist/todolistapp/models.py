from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class note(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length = 255)
    date = models.CharField(max_length = 255)
    desc = models.CharField(max_length = 255)
    
    
