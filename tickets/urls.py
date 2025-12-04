from django.urls import path
from .views import (
    TicketListCreateView,
    TicketDetailView,
    TicketCommentCreateView
)

urlpatterns = [
    path('', TicketListCreateView.as_view(), name='tickets'),
    path('<int:pk>/', TicketDetailView.as_view(), name='ticket-detail'),
    path('<int:ticket_id>/comments/', TicketCommentCreateView.as_view(), name='ticket-comment'),
]
