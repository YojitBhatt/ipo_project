from django.urls import path
from .views import IPOListAPIView, IPODetailAPIView

urlpatterns = [
    path('api/ipo/', IPOListAPIView.as_view()),
    path('api/ipo/<int:pk>/', IPODetailAPIView.as_view()),
]

