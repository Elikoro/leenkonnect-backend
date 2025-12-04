from django.db import models
from django.conf import settings

User = settings.AUTH_USER_MODEL


class DailyAnalyticsSnapshot(models.Model):
    """
    Daily snapshot of organization-wide metrics.
    This gives you historical analytics & trend data.
    """

    organization = models.ForeignKey(
        "organizations.Organization",
        on_delete=models.CASCADE,
        related_name="daily_analytics",
    )

    date = models.DateField(auto_now_add=True)

    # Project analytics
    total_projects = models.IntegerField(default=0)
    active_projects = models.IntegerField(default=0)
    completed_projects = models.IntegerField(default=0)

    # Tickets analytics
    total_tickets = models.IntegerField(default=0)
    open_tickets = models.IntegerField(default=0)
    in_progress_tickets = models.IntegerField(default=0)
    closed_tickets = models.IntegerField(default=0)

    # Financial analytics
    total_invoices = models.IntegerField(default=0)
    paid_invoices = models.IntegerField(default=0)
    unpaid_invoices = models.IntegerField(default=0)
    revenue = models.FloatField(default=0)
    outstanding_balance = models.FloatField(default=0)

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ("organization", "date")
        ordering = ("-date",)

    def __str__(self):
        return f"{self.organization.name} — {self.date}"


class TechnicianProductivitySnapshot(models.Model):
    """
    Stores daily performance metrics for each technician.
    """

    technician = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="productivity_snapshots"
    )
    organization = models.ForeignKey(
        "organizations.Organization",
        on_delete=models.CASCADE,
        related_name="technician_productivity",
    )

    date = models.DateField(auto_now_add=True)

    tickets_assigned = models.IntegerField(default=0)
    tickets_closed = models.IntegerField(default=0)
    avg_resolution_hours = models.FloatField(default=0)

    projects_assigned = models.IntegerField(default=0)
    projects_completed = models.IntegerField(default=0)

    productivity_score = models.FloatField(default=0)

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ("technician", "date")
        ordering = ("-date",)

    def __str__(self):
        return f"{self.technician} — {self.date}"


class FinancialAnalyticsSnapshot(models.Model):
    """
    Stores daily billing/economics analytics for finance dashboards.
    """

    organization = models.ForeignKey(
        "organizations.Organization",
        on_delete=models.CASCADE,
        related_name="daily_financials",
    )

    date = models.DateField(auto_now_add=True)

    total_invoices = models.IntegerField(default=0)
    paid_invoices = models.IntegerField(default=0)
    unpaid_invoices = models.IntegerField(default=0)

    total_revenue = models.FloatField(default=0)
    outstanding_balance = models.FloatField(default=0)
    paid_today = models.FloatField(default=0)
    unpaid_today = models.FloatField(default=0)

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ("organization", "date")
        ordering = ("-date",)

    def __str__(self):
        return f"{self.organization.name} — Finance {self.date}"
