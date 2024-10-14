# users/serializers.py

from rest_framework import serializers
from .models import CustomUser

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'first_name', 'last_name', 'email', 'is_student', 'is_consultant']  # فیلدهای مورد نیاز
        read_only_fields = ['id']  # این فیلد فقط برای خواندن است

    def create(self, validated_data):
        return CustomUser.objects.create_user(**validated_data)  # ایجاد کاربر جدید

    def update(self, instance, validated_data):
        # بروزرسانی داده‌های کاربر
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        return instance
