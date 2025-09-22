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
from django.http import JsonResponse

def api_root(request):
    """API root endpoint with available endpoints information"""
    return JsonResponse({
        'message': 'Django REST API - Employee Management System',
        'version': '1.0.0',
        'endpoints': {
            'admin': '/admin/',
            'employees': {
                'list': '/api/employees/',
                'create': 'POST /api/employees/',
                'detail': '/api/employees/{id}/',
                'update': 'PUT /api/employees/{id}/',
                'delete': 'DELETE /api/employees/{id}/'
            }
        },
        'documentation': 'This API provides CRUD operations for employee management'
    })

urlpatterns = [
    path('', api_root, name='api-root'),
    path('admin/', admin.site.urls),
    path('api/employees/', include('employees.urls')),
]
