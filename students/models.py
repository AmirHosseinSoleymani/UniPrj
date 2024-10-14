from django.db import models
from users.models import CustomUser
from consultants.models import Consultant

class Student(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE,null=True, blank=True)
    father_name = models.CharField(max_length=100)
    national_code = models.CharField(max_length=10, unique=True)
    city = models.CharField(max_length=100)
    province = models.CharField(max_length=100)
    mobile = models.CharField(max_length=15)
    address = models.TextField()
    birth_date = models.DateField()
    weekly_program = models.TextField(blank=True, null=True)
    consultant = models.ForeignKey(Consultant, on_delete=models.SET_NULL, null=True)
    registration_date = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name}'