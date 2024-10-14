
from rest_framework import generics
from .models import Consultant
from .serializer import ConsultantSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication

class ConsultantListCreateView(generics.ListCreateAPIView):
    queryset = Consultant.objects.all()
    serializer_class = ConsultantSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

class ConsultantRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Consultant.objects.all()
    serializer_class = ConsultantSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
