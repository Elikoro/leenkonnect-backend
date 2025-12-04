from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from projects.models import Project
from tickets.models import Ticket
from billing.models import Invoice
from django.db import models
from .serializers import (
    ProjectAnalyticsSerializer,
    TicketAnalyticsSerializer,
    FinancialAnalyticsSerializer,
)


class ProjectAnalyticsView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        org = user.organization

        projects = Project.objects.filter(organization=org)

        total_projects = projects.count()
        active_projects = projects.filter(status="in_progress").count()
        completed_projects = projects.filter(status="completed").count()

        completion_rate = (
            (completed_projects / total_projects) * 100 if total_projects > 0 else 0
        )

        avg_duration = projects.filter(end_date__isnull=False).annotate(
            duration=models.F("end_date") - models.F("start_date")
        ).aggregate(avg=models.Avg("duration"))["avg"]

        data = {
            "total_projects": total_projects,
            "active_projects": active_projects,
            "completed_projects": completed_projects,
            "completion_rate": round(completion_rate, 2),
            "avg_duration_days": round(avg_duration.days, 2) if avg_duration else 0,
        }

        serializer = ProjectAnalyticsSerializer(data)
        return Response(serializer.data)


class TicketAnalyticsView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        org = user.organization

        tickets = Ticket.objects.filter(organization=org)

        total = tickets.count()
        open_tickets = tickets.filter(status="open").count()
        in_progress = tickets.filter(status="in_progress").count()
        closed = tickets.filter(status="closed").count()

        avg_resolution = tickets.filter(
            closed_at__isnull=False
        ).annotate(
            duration=models.F("closed_at") - models.F("created_at")
        ).aggregate(avg=models.Avg("duration"))["avg"]

        data = {
            "total_tickets": total,
            "open_tickets": open_tickets,
            "in_progress": in_progress,
            "closed_tickets": closed,
            "avg_resolution_hours": round(avg_resolution.total_seconds() / 3600, 2)
            if avg_resolution else 0,
        }

        serializer = TicketAnalyticsSerializer(data)
        return Response(serializer.data)


class FinancialAnalyticsView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        org = user.organization

        invoices = Invoice.objects.filter(organization=org)

        total_invoices = invoices.count()
        paid = invoices.filter(status="paid").count()
        unpaid = invoices.filter(status="unpaid").count()

        revenue = invoices.filter(status="paid").aggregate(total=models.Sum("amount"))[
            "total"
        ] or 0

        outstanding = invoices.filter(status="unpaid").aggregate(
            total=models.Sum("amount")
        )["total"] or 0

        data = {
            "total_invoices": total_invoices,
            "paid_invoices": paid,
            "unpaid_invoices": unpaid,
            "total_revenue": revenue,
            "outstanding_balance": outstanding,
        }

        serializer = FinancialAnalyticsSerializer(data)
        return Response(serializer.data)
