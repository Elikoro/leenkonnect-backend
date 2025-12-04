from django.urls import path
from .views import (
    ProjectAnalyticsView,
    TicketAnalyticsView,
    FinancialAnalyticsView,
)

urlpatterns = [
    path("projects/", ProjectAnalyticsView.as_view()),
    path("tickets/", TicketAnalyticsView.as_view()),
    path("financials/", FinancialAnalyticsView.as_view()),
]
