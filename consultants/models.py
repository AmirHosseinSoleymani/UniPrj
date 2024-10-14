from django.db import models
from users.models import CustomUser

class Consultant(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE,null=True, blank=True)
    city = models.CharField(max_length=100)
    province = models.CharField(max_length=100)
    mobile = models.CharField(max_length=15)
    address = models.TextField()
    registration_date = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    national_code = models.CharField(max_length=10, unique=True)

    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name}'
