"""
URL configuration for django_rest_main project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenRefreshView

from employees.views import (
    EmployeeViewSet,
    register_user,
    MyTokenObtainPairView,
    UserListAPIView
)

# The router automatically generates the URL patterns for the EmployeeViewSet.
router = DefaultRouter()
router.register(r'employees', EmployeeViewSet, basename='employee')

# Main URL patterns for the entire project.
urlpatterns = [
    # Redirect the root URL to the main API endpoint.
    path('', lambda request: redirect('api/', permanent=True)),

    # Django admin site.
    path('admin/', admin.site.urls),

    # All API endpoints will be prefixed with 'api/'.
    path('api/', include([
        # URLs for user registration and authentication.
        path("register/", register_user, name="register"),
        path("users/", UserListAPIView.as_view(), name="user-list"),
        path('token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
        path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

        # Include the router-generated URLs for the EmployeeViewSet.
        # This will create endpoints like /api/employees/ and /api/employees/<employee_id>/
        path('', include(router.urls)),
    ])),
]

# from django.contrib import admin
# from django.urls import path, include
# from rest_framework.routers import DefaultRouter
# from employees.views import EmployeeViewSet, register_user, MyTokenObtainPairView
# from employees.views import UserListAPIView
# from rest_framework_simplejwt.views import TokenRefreshView
# from django.conf import settings
# from django.conf.urls.static import static
# from employees import views
# from django.shortcuts import redirect

# router = DefaultRouter()
# router.register(r'employees', EmployeeViewSet)

# urlpatterns = [
#     path('', lambda request: redirect('/api/')),
#     path('admin/', admin.site.urls),
#     path('api/employees/', views.employee_list),
#     path('api/', include(router.urls)),
#     path("api/users/", UserListAPIView.as_view(), name="user-list"),
#     path("api/register/", register_user, name="signup"),
#     path('api/token/',  MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
#     path('api/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
# ]