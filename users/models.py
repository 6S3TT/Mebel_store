from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    email = models.EmailField('email address', unique=True)
    phone_number = models.CharField(max_length=15, unique=True)
    USERNAME_FIELD = 'email'



class Profile(models.Model):
    city = models.CharField(max_length=40)
    street = models.CharField(max_length=70)
    suite = models.CharField(max_length=50)
    apartment = models.CharField(max_length=50)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name} Profile'





