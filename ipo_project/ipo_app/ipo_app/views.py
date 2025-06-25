from rest_framework import generics
from .models import IPO
from .serializers import IPOSerializer

class IPOListAPIView(generics.ListAPIView):
    queryset = IPO.objects.all()
    serializer_class = IPOSerializer

class IPODetailAPIView(generics.RetrieveAPIView):
    queryset = IPO.objects.all()
    serializer_class = IPOSerializer
