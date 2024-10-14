from rest_framework import serializers
from .models import Lesson, DailyLesson, Break

# سریالایزر برای Lesson
class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = ['id', 'name', 'grade', 'level']  # فیلدهای مورد نیاز برای درس

# سریالایزر برای DailyLesson
class DailyLessonSerializer(serializers.ModelSerializer):
    lesson = LessonSerializer()  # سریالایزر برای درس

    class Meta:
        model = DailyLesson
        fields = ['id', 'daily_program', 'lesson', 'allocated_time', 'break_time', 'start_time', 'end_time', 'completion_status']

    def create(self, validated_data):
        lesson_data = validated_data.pop('lesson')  # جدا کردن داده‌های درس
        lesson, _ = Lesson.objects.get_or_create(**lesson_data)  # پیدا کردن یا ایجاد درس
        daily_lesson = DailyLesson.objects.create(lesson=lesson, **validated_data)  # ایجاد درس روزانه
        return daily_lesson

    def update(self, instance, validated_data):
        lesson_data = validated_data.get('lesson')
        if lesson_data:
            lesson, _ = Lesson.objects.get_or_create(**lesson_data)  # پیدا کردن یا ایجاد درس
            instance.lesson = lesson

        # بروزرسانی سایر فیلدها
        for attr, value in validated_data.items():
            if attr != 'lesson':
                setattr(instance, attr, value)
        instance.save()
        return instance

    def validate(self, data):
        """اعتبارسنجی زمان شروع و پایان"""
        if data['start_time'] >= data['end_time']:
            raise serializers.ValidationError("زمان شروع باید قبل از زمان پایان باشد.")
        return data

# سریالایزر برای Break
class BreakSerializer(serializers.ModelSerializer):
    lesson1 = DailyLessonSerializer()  # سریالایزر برای درس اول
    lesson2 = DailyLessonSerializer()  # سریالایزر برای درس دوم

    class Meta:
        model = Break
        fields = ['id', 'daily_program', 'duration', 'lesson1', 'lesson2']

    def create(self, validated_data):
        lesson1_data = validated_data.pop('lesson1')  # جدا کردن داده‌های درس اول
        lesson2_data = validated_data.pop('lesson2')  # جدا کردن داده‌های درس دوم
        
        # پیدا کردن یا ایجاد درس‌ها
        lesson1, _ = DailyLesson.objects.get_or_create(**lesson1_data)
        lesson2, _ = DailyLesson.objects.get_or_create(**lesson2_data)
        
        # ایجاد استراحت
        break_instance = Break.objects.create(lesson1=lesson1, lesson2=lesson2, **validated_data)
        return break_instance

    def update(self, instance, validated_data):
        lesson1_data = validated_data.get('lesson1')
        lesson2_data = validated_data.get('lesson2')

        if lesson1_data:
            lesson1, _ = DailyLesson.objects.get_or_create(**lesson1_data)
            instance.lesson1 = lesson1

        if lesson2_data:
            lesson2, _ = DailyLesson.objects.get_or_create(**lesson2_data)
            instance.lesson2 = lesson2

        # بروزرسانی سایر فیلدها
        for attr, value in validated_data.items():
            if attr not in ['lesson1', 'lesson2']:
                setattr(instance, attr, value)
        instance.save()
        return instance

    def validate(self, data):
        """اعتبارسنجی مدت زمان استراحت"""
        if data['duration'].total_seconds() <= 0:
            raise serializers.ValidationError("مدت زمان استراحت باید بیشتر از صفر باشد.")
        return data
