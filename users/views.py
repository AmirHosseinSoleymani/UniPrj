
from rest_framework import generics
from .models import CustomUser
from .serializer import CustomUserSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication

# ویو برای لیست کردن و ایجاد کاربران
class CustomUserListCreateView(generics.ListCreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

# ویو برای مشاهده، به‌روزرسانی و حذف یک کاربر خاص
class CustomUserRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
