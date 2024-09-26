from django.db import models

class ServiceRequest(models.Model):
    """
    Represents a service request made by a customer, including contact details, 
    service type, and description of the request.
    """
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    service_type = models.CharField(max_length=100)  # choices can be added for specific service types
    description = models.TextField()
    date = models.DateTimeField(auto_now_add=True)  # Automatically sets the current date and time
    status = models.CharField(max_length=20, default='Pending')  # You can use choices for different statuses

    def __str__(self):
        """
        Return a string representation of the service request.
        """
        return f"Service Request from {self.name} on {self.date}"
