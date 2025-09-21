from django.contrib import admin
from .models import Employee

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['employee_id', 'name', 'email', 'contact', 'created_at']
    list_filter = ['created_at', 'updated_at']
    search_fields = ['employee_id', 'name', 'email']
    readonly_fields = ['created_at', 'updated_at']
    ordering = ['-created_at']
