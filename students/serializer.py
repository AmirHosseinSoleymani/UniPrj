from rest_framework import serializers
from users.models import CustomUser
from consultants.models import Consultant
from .models import Student

# سریالایزر برای CustomUser
class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'first_name', 'last_name', 'email']  # فیلدهای مورد نیاز از مدل CustomUser

    def create(self, validated_data):
        return CustomUser.objects.create(**validated_data)

    def update(self, instance, validated_data):
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        return instance

# سریالایزر برای Consultant
class ConsultantSerializer(serializers.ModelSerializer):
    user = CustomUserSerializer()

    class Meta:
        model = Consultant
        fields = ['user', 'city', 'province', 'mobile']

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user = CustomUser.objects.create(**user_data)
        consultant = Consultant.objects.create(user=user, **validated_data)
        return consultant

    def update(self, instance, validated_data):
        user_data = validated_data.pop('user', None)
        if user_data:
            # بروزرسانی کاربر
            user_serializer = CustomUserSerializer(instance=instance.user, data=user_data)
            if user_serializer.is_valid(raise_exception=True):
                user_serializer.save()

        # بروزرسانی سایر فیلدها
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        return instance

# سریالایزر اصلی برای Student
class StudentSerializer(serializers.ModelSerializer):
    user = CustomUserSerializer()  # سریالایزر CustomUser برای نمایش اطلاعات کاربر
    consultant = ConsultantSerializer()  # سریالایزر Consultant برای نمایش اطلاعات مشاور

    class Meta:
        model = Student
        fields = ['user', 'father_name', 'national_code', 'city', 'province', 'mobile', 'address', 'birth_date', 'weekly_program', 'consultant', 'registration_date', 'updated_at']
        read_only_fields = ['registration_date', 'updated_at']  # فیلدهای فقط خواندنی

    def create(self, validated_data):
        user_data = validated_data.pop('user')  # جدا کردن داده‌های کاربر
        user_serializer = CustomUserSerializer(data=user_data)
        if user_serializer.is_valid(raise_exception=True):
            user = user_serializer.save()

        consultant_data = validated_data.pop('consultant', None)
        consultant = None
        if consultant_data:
            consultant_serializer = ConsultantSerializer(data=consultant_data)
            if consultant_serializer.is_valid(raise_exception=True):
                consultant = consultant_serializer.save()

        student = Student.objects.create(user=user, consultant=consultant, **validated_data)  # ایجاد دانش‌آموز
        return student

    def update(self, instance, validated_data):
        user_data = validated_data.get('user')
        if user_data:
            # بروزرسانی کاربر
            user_serializer = CustomUserSerializer(instance=instance.user, data=user_data)
            if user_serializer.is_valid(raise_exception=True):
                user_serializer.save()

        consultant_data = validated_data.get('consultant')
        if consultant_data:
            # بروزرسانی مشاور
            consultant_serializer = ConsultantSerializer(instance=instance.consultant, data=consultant_data)
            if consultant_serializer.is_valid(raise_exception=True):
                consultant_serializer.save()

        # به‌روزرسانی سایر فیلدهای دانش‌آموز
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        return instance

    def validate_mobile(self, value):
        """اعتبارسنجی برای شماره موبایل"""
        if not value.isdigit() or len(value) != 10:  # شماره موبایل باید 10 رقمی باشد
            raise serializers.ValidationError("شماره موبایل نامعتبر است.")
        return value

    def validate_national_code(self, value):
        """اعتبارسنجی برای کد ملی"""
        if len(value) != 10 or not value.isdigit():
            raise serializers.ValidationError("کد ملی باید 10 رقم باشد.")
        return value
