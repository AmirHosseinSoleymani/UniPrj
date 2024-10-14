from rest_framework import generics
from .models import WeeklyProgram, DailyProgram
from .serializer import WeeklyProgramSerializer, DailyProgramSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication

# ویو برای لیست کردن و ایجاد WeeklyProgram
class WeeklyProgramListCreateView(generics.ListCreateAPIView):
    queryset = WeeklyProgram.objects.all()
    serializer_class = WeeklyProgramSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

# ویو برای مشاهده، به‌روزرسانی و حذف WeeklyProgram
class WeeklyProgramRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = WeeklyProgram.objects.all()
    serializer_class = WeeklyProgramSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

# ویو برای لیست کردن و ایجاد DailyProgram
class DailyProgramListCreateView(generics.ListCreateAPIView):
    queryset = DailyProgram.objects.all()
    serializer_class = DailyProgramSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

# ویو برای مشاهده، به‌روزرسانی و حذف DailyProgram
class DailyProgramRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = DailyProgram.objects.all()
    serializer_class = DailyProgramSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
