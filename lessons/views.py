
from rest_framework import generics
from .models import Lesson, DailyLesson, Break
from .serializer import LessonSerializer, DailyLessonSerializer, BreakSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication

# ویو برای لیست کردن و ایجاد درس‌ها
class LessonListCreateView(generics.ListCreateAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

# ویو برای مشاهده، به‌روزرسانی و حذف یک درس خاص
class LessonRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

# ویو برای لیست کردن و ایجاد درس‌های روزانه
class DailyLessonListCreateView(generics.ListCreateAPIView):
    queryset = DailyLesson.objects.all()
    serializer_class = DailyLessonSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

# ویو برای مشاهده، به‌روزرسانی و حذف یک درس روزانه خاص
class DailyLessonRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = DailyLesson.objects.all()
    serializer_class = DailyLessonSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

# ویو برای لیست کردن و ایجاد استراحت‌ها
class BreakListCreateView(generics.ListCreateAPIView):
    queryset = Break.objects.all()
    serializer_class = BreakSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

# ویو برای مشاهده، به‌روزرسانی و حذف یک استراحت خاص
class BreakRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Break.objects.all()
    serializer_class = BreakSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

