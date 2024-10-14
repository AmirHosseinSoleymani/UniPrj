from django.db import models
from students.models import Student
from consultants.models import Consultant

class WeeklyProgram(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    consultant = models.ForeignKey(Consultant, on_delete=models.CASCADE)
    progress_status = models.DecimalField(max_digits=5, decimal_places=2)  # درصد پیشرفت
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return f'Program for {self.student.first_name} {self.student.last_name}'



class DailyProgram(models.Model):
    weekly_program = models.ForeignKey(WeeklyProgram, on_delete=models.CASCADE)
    progress_status = models.DecimalField(max_digits=5, decimal_places=2)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return f'Daily Program for Weekly Program {self.weekly_program.id}'
