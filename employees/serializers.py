from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from .models import Employee

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token["username"] = user.username
        token["email"] = user.email
        return token

class UserRegistrationSerializer(serializers.ModelSerializer):
    """
    Serializer for handling new user registration. Includes password confirmation.
    """
    password = serializers.CharField(write_only=True, required=True)
    confirm_password = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'password', 'confirm_password')

    def validate(self, attrs):
        if attrs['password'] != attrs['confirm_password']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})
        return attrs
    
    def validate_email(self, value):
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError("A user with this email already exists.")
        return value

    def create(self, validated_data):
        # Remove the confirm_password field as it's not part of the User model
        validated_data.pop('confirm_password')
        user = User.objects.create_user(**validated_data)
        return user

class UserSerializer(serializers.ModelSerializer):
    """
    Serializer for listing user information safely.
    """
    class Meta:
        model = User
        fields = ('username', 'email')

# --- Employee Serializer ---

class EmployeeSerializer(serializers.ModelSerializer):
    """
    Serializer for the Employee model.
    """
    class Meta:
        model = Employee
        fields = ['employee_id', 'employee_name', 'employee_email', 'employee_contact']

    def validate_employee_id(self, value):
        """Validate that employee_id is unique."""
        # 'self.instance' is the object being updated, if any.
        # This check allows the same ID when updating the same employee.
        if self.instance and self.instance.employee_id == value:
            return value
        if Employee.objects.filter(employee_id=value).exists():
            raise serializers.ValidationError("An employee with this ID already exists.")
        return value

    def validate_employee_email(self, value):
        """Validate that employee_email is unique."""
        if self.instance and self.instance.employee_email == value:
            return value
        if Employee.objects.filter(employee_email=value).exists():
            raise serializers.ValidationError("An employee with this email already exists.")
        return value
