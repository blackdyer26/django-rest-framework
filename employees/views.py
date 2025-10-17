from rest_framework import viewsets, generics
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView 
from django.contrib.auth.models import User

from .models import Employee
from .serializers import (
    EmployeeSerializer,
    UserRegistrationSerializer,
    MyTokenObtainPairSerializer,      
    MyTokenRefreshSerializer        
)
class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer
class MyTokenRefreshView(TokenRefreshView):
    serializer_class = MyTokenRefreshSerializer
class UserCreateView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserRegistrationSerializer
    permission_classes = [AllowAny] 
class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    permission_classes = [IsAuthenticated]
