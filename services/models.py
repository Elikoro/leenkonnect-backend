from django.db import models
from django.conf import settings
from organizations.models import Organization

class Service(models.Model):
    SERVICE_TYPES = [
        ('network', 'Network Setup'),
        ('cloud', 'Cloud Service'),
        ('repair', 'Device Repair'),
        ('software', 'Software Setup'),
        ('consult', 'IT Consultation'),
    ]

    organization = models.ForeignKey(Organization, on_delete=models.CASCADE, related_name="services")
    name = models.CharField(max_length=255)
    type = models.CharField(max_length=50, choices=SERVICE_TYPES)
    description = models.TextField()
    base_price = models.DecimalField(max_digits=10, decimal_places=2)
    active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class WorkOrder(models.Model):
    STATUS = [
        ('pending', 'Pending'),
        ('assigned', 'Assigned'),
        ('in_progress', 'In Progress'),
        ('completed', 'Completed'),
        ('cancelled', 'Cancelled')
    ]

    organization = models.ForeignKey(Organization, on_delete=models.CASCADE, related_name="work_orders")
    service = models.ForeignKey(Service, on_delete=models.CASCADE, related_name="work_orders")
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)
    assigned_to = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        related_name="assigned_work_orders"
    )

    description = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS, default='pending')
    due_date = models.DateField(null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"WorkOrder #{self.id} — {self.service.name}"
