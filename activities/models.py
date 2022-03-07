from django.db import models
from django.conf import settings
from django.utils import timezone
from django.contrib.auth.models import User , AbstractUser

class CustomUser(AbstractUser):
    username = models.CharField(max_length=40, unique=True)
    email = models.EmailField(unique=True)
    birth_date = models.DateField(null=True)
    phone_number = models.IntegerField(null=True)

    def __str__(self):   
        return self.username


# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length = 255)
    text = models.CharField(max_length = 255 * 4)
    made_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    posted = models.DateField(default = timezone.now)

    def __str__(self):
            return self.title