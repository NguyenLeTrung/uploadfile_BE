from django.db import models
from django.contrib.auth.models import AbstractBaseUser

# Create your models here.
class User(AbstractBaseUser):
    username = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=100)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

class UploadFile(models.Model):
    folder = models.CharField(max_length=255, null=True)
    file = models.FileField(upload_to="upload")
    create_date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, related_name="User", on_delete=models.CASCADE, null=True)