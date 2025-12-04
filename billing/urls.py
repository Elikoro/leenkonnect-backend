from django.urls import path
from .views import (
    InvoiceListCreateView,
    InvoiceDetailView,
    InvoiceItemCreateView,
    PaymentCreateView
)

urlpatterns = [
    path('', InvoiceListCreateView.as_view(), name='invoices'),
    path('<int:pk>/', InvoiceDetailView.as_view(), name='invoice-detail'),
    path('<int:invoice_id>/items/', InvoiceItemCreateView.as_view(), name='invoice-items'),
    path('<int:invoice_id>/payments/', PaymentCreateView.as_view(), name='invoice-payments'),
]
