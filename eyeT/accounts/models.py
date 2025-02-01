from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)  # Ensure email is unique
    date_of_birth = models.DateField(null=True, blank=True)
    age = models.IntegerField(null=True, blank=True)
    gender = models.CharField(max_length=10, choices=[('Male', 'Male'), ('Female', 'Female')], null=True, blank=True)

    REQUIRED_FIELDS = ['username', 'date_of_birth', 'age', 'gender']
    USERNAME_FIELD = 'email'  # Use email as the unique identifier for login

    def __str__(self):
        return self.email