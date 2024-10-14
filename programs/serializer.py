from rest_framework import serializers
from .models import WeeklyProgram, DailyProgram
from students.serializer import StudentSerializer
from consultants.serializer import ConsultantSerializer

# سریالایزر برای WeeklyProgram
class WeeklyProgramSerializer(serializers.ModelSerializer):
    student = StudentSerializer()  # سریالایزر برای دانش‌آموز
    consultant = ConsultantSerializer()  # سریالایزر برای مشاور

    class Meta:
        model = WeeklyProgram
        fields = ['id', 'student', 'consultant', 'progress_status', 'created_at', 'updated_at']
        read_only_fields = ['created_at', 'updated_at']  # فیلدهای فقط خواندنی

    def create(self, validated_data):
        student_data = validated_data.pop('student')  # جدا کردن داده‌های دانش‌آموز
        consultant_data = validated_data.pop('consultant')  # جدا کردن داده‌های مشاور

        student_serializer = StudentSerializer(data=student_data)
        consultant_serializer = ConsultantSerializer(data=consultant_data)

        if student_serializer.is_valid(raise_exception=True) and consultant_serializer.is_valid(raise_exception=True):
            student = student_serializer.save()  # ایجاد دانش‌آموز
            consultant = consultant_serializer.save()  # ایجاد مشاور

        weekly_program = WeeklyProgram.objects.create(student=student, consultant=consultant, **validated_data)
        return weekly_program

    def update(self, instance, validated_data):
        student_data = validated_data.get('student')
        consultant_data = validated_data.get('consultant')

        if student_data:
            student_serializer = StudentSerializer(instance=instance.student, data=student_data)
            if student_serializer.is_valid(raise_exception=True):
                student_serializer.save()

        if consultant_data:
            consultant_serializer = ConsultantSerializer(instance=instance.consultant, data=consultant_data)
            if consultant_serializer.is_valid(raise_exception=True):
                consultant_serializer.save()

        # بروزرسانی سایر فیلدها
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        return instance

    def validate_progress_status(self, value):
        """اعتبارسنجی برای درصد پیشرفت"""
        if value < 0 or value > 100:
            raise serializers.ValidationError("درصد پیشرفت باید بین 0 تا 100 باشد.")
        return value


# سریالایزر برای DailyProgram
class DailyProgramSerializer(serializers.ModelSerializer):
    weekly_program = WeeklyProgramSerializer()  # سریالایزر برای برنامه هفتگی

    class Meta:
        model = DailyProgram
        fields = ['id', 'weekly_program', 'progress_status', 'created_at', 'updated_at']
        read_only_fields = ['created_at', 'updated_at']  # فیلدهای فقط خواندنی

    def create(self, validated_data):
        weekly_program_data = validated_data.pop('weekly_program')  # جدا کردن داده‌های برنامه هفتگی
        weekly_program_serializer = WeeklyProgramSerializer(data=weekly_program_data)

        if weekly_program_serializer.is_valid(raise_exception=True):
            weekly_program = weekly_program_serializer.save()

        daily_program = DailyProgram.objects.create(weekly_program=weekly_program, **validated_data)
        return daily_program

    def update(self, instance, validated_data):
        weekly_program_data = validated_data.get('weekly_program')

        if weekly_program_data:
            weekly_program_serializer = WeeklyProgramSerializer(instance=instance.weekly_program, data=weekly_program_data)
            if weekly_program_serializer.is_valid(raise_exception=True):
                weekly_program_serializer.save()

        # بروزرسانی سایر فیلدها
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        return instance

    def validate_progress_status(self, value):
        """اعتبارسنجی برای درصد پیشرفت"""
        if value < 0 or value > 100:
            raise serializers.ValidationError("درصد پیشرفت باید بین 0 تا 100 باشد.")
        return value
