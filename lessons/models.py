from django.db import models
from programs.models import *

class Lesson(models.Model):
    name = models.CharField(max_length=100)
    grade = models.CharField(max_length=50)
    level = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    
class DailyLesson(models.Model):
    daily_program = models.ForeignKey(DailyProgram, on_delete=models.CASCADE)
    lesson = models.ForeignKey(Lesson, on_delete=models.SET_NULL, null=True)
    allocated_time = models.DurationField()  # مدت زمان تعیین شده
    break_time = models.DurationField()  # میزان وقفه
    start_time = models.TimeField()
    end_time = models.TimeField()
    completion_status = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.lesson.name} for Daily Program {self.daily_program.id}'


class Break(models.Model):
    daily_program = models.ForeignKey(DailyProgram, on_delete=models.CASCADE)
    duration = models.DurationField()
    lesson1 = models.ForeignKey(DailyLesson, related_name='lesson1_break', on_delete=models.SET_NULL, null=True)
    lesson2 = models.ForeignKey(DailyLesson, related_name='lesson2_break', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f'Break in Daily Program {self.daily_program.id}'




