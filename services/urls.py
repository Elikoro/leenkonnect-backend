from django.urls import path
from .views import (
    ServiceListCreateView,
    WorkOrderListCreateView,
    WorkOrderDetailView
)

urlpatterns = [
    path('services/', ServiceListCreateView.as_view(), name='services'),
    path('work-orders/', WorkOrderListCreateView.as_view(), name='work-orders'),
    path('work-orders/<int:pk>/', WorkOrderDetailView.as_view(), name='work-order-detail'),
]
