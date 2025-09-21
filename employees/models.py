from django.db import models

class Employee(models.Model):
    employee_id = models.CharField(max_length=50, unique=True, help_text="Unique employee identifier")
    name = models.CharField(max_length=100, help_text="Full name of the employee")
    email = models.EmailField(unique=True, help_text="Email address of the employee")
    contact = models.CharField(max_length=15, help_text="Contact number of the employee")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name = "Employee"
        verbose_name_plural = "Employees"

    def __str__(self):
        return f"{self.name} ({self.employee_id})"
