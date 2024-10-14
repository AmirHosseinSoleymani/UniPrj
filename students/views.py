
from rest_framework import generics
from .models import Student
from .serializer import StudentSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication


class StudentListCreateView(generics.ListCreateAPIView):
    queryset = Student.objects.all()  
    serializer_class = StudentSerializer  
    authentication_classes = [TokenAuthentication] 
    permission_classes = [IsAuthenticated]  


class StudentRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()  
    serializer_class = StudentSerializer  
    authentication_classes = [TokenAuthentication]  
    permission_classes = [IsAuthenticated]  

