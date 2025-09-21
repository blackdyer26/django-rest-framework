from django.urls import path
from . import views

urlpatterns = [
    # Class-based views (recommended)
    path('', views.EmployeeListCreateView.as_view(), name='employee-list-create'),
    path('<int:id>/', views.EmployeeRetrieveUpdateDestroyView.as_view(), name='employee-detail'),
    
    # Alternative function-based views
    # path('list/', views.employee_list, name='employee-list'),
    # path('create/', views.employee_create, name='employee-create'),
    # path('<int:pk>/', views.employee_detail, name='employee-detail'),
]
