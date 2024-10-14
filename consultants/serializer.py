from rest_framework import serializers
from users.models import CustomUser
from .models import Consultant

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'first_name', 'last_name', 'email']

    def create(self, validated_data):
        return CustomUser.objects.create(**validated_data)

    def update(self, instance, validated_data):
        # بروزرسانی داده‌های کاربر
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        return instance


class ConsultantSerializer(serializers.ModelSerializer):
    user = CustomUserSerializer()

    class Meta:
        model = Consultant
        fields = ['user', 'city', 'province', 'mobile', 'address', 'national_code', 'registration_date', 'updated_at']
        read_only_fields = ['registration_date', 'updated_at']

    def create(self, validated_data):
        user_data = validated_data.pop('user')  # داده‌های کاربر را جدا کن
        user_serializer = CustomUserSerializer(data=user_data)
        if user_serializer.is_valid(raise_exception=True):
            user = user_serializer.save()  # ایجاد کاربر با استفاده از سریالایزر
        consultant = Consultant.objects.create(user=user, **validated_data)  # ایجاد مشاور
        return consultant

    def update(self, instance, validated_data):
        user_data = validated_data.get('user')  # دریافت داده‌های کاربر بدون حذف آن
        if user_data:
            # بروزرسانی کاربر از طریق سریالایزر
            user_serializer = CustomUserSerializer(instance=instance.user, data=user_data)
            if user_serializer.is_valid(raise_exception=True):
                user_serializer.save()

        # بروزرسانی سایر فیلدهای مشاور
        for attr, value in validated_data.items():
            if attr != 'user':  # جلوگیری از دوباره ست کردن فیلد کاربر
                setattr(instance, attr, value)
        instance.save()
        return instance

    def validate_mobile(self, value):
        """اعتبارسنجی برای شماره موبایل"""
        if not value.isdigit() or len(value) != 10:
            raise serializers.ValidationError("شماره موبایل نامعتبر است.")
        return value

    def validate_national_code(self, value):
        """اعتبارسنجی برای کد ملی"""
        if len(value) != 10 or not value.isdigit():
            raise serializers.ValidationError("کد ملی باید 10 رقم باشد.")
        return value
