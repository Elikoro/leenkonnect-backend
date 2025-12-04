from rest_framework import serializers


class ProjectAnalyticsSerializer(serializers.Serializer):
    total_projects = serializers.IntegerField()
    active_projects = serializers.IntegerField()
    completed_projects = serializers.IntegerField()
    completion_rate = serializers.FloatField()
    avg_duration_days = serializers.FloatField()


class TicketAnalyticsSerializer(serializers.Serializer):
    total_tickets = serializers.IntegerField()
    open_tickets = serializers.IntegerField()
    in_progress = serializers.IntegerField()
    closed_tickets = serializers.IntegerField()
    avg_resolution_hours = serializers.FloatField()


class FinancialAnalyticsSerializer(serializers.Serializer):
    total_invoices = serializers.IntegerField()
    paid_invoices = serializers.IntegerField()
    unpaid_invoices = serializers.IntegerField()
    total_revenue = serializers.FloatField()
    outstanding_balance = serializers.FloatField()
