from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    date_of_birth = models.DateField(null=True, blank=True),
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True),
    city = models.CharField(max_length=36, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'Profile'
