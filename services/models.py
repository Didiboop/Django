

from django.db import models

class ServiceRequest(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    service_type = models.CharField(max_length=100)  # choices here for specific service types
    description = models.TextField()
    date = models.DateTimeField(auto_now_add=True)  # Automatically sets the current date and time
    status = models.CharField(max_length=20, default='Pending')  # You can use choices here for different statuses

    def __str__(self):
        return f"Service Request from {self.name} on {self.date}"
