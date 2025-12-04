def generate_invoice_number(org):
    count = Invoice.objects.filter(organization=org).count() + 1
    return f"INV-{org.id}-{count:05d}"

from rest_framework import generics, permissions
from .models import Invoice, InvoiceItem, Payment
from .serializers import InvoiceSerializer, InvoiceItemSerializer, PaymentSerializer


class InvoiceListCreateView(generics.ListCreateAPIView):
    serializer_class = InvoiceSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Invoice.objects.filter(organization=self.request.user.organization)

    def perform_create(self, serializer):
        invoice_number = generate_invoice_number(self.request.user.organization)

        serializer.save(
            organization=self.request.user.organization,
            invoice_number=invoice_number
        )

class InvoiceDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = InvoiceSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Invoice.objects.filter(organization=self.request.user.organization)

class InvoiceItemCreateView(generics.CreateAPIView):
    serializer_class = InvoiceItemSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        invoice_id = self.kwargs['invoice_id']
        invoice = Invoice.objects.get(
            id=invoice_id,
            organization=self.request.user.organization
        )
        serializer.save(invoice=invoice)

        # After saving, update invoice totals
        update_invoice_totals(invoice)

class PaymentCreateView(generics.CreateAPIView):
    serializer_class = PaymentSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        invoice_id = self.kwargs['invoice_id']
        invoice = Invoice.objects.get(
            id=invoice_id,
            organization=self.request.user.organization
        )
        serializer.save(invoice=invoice)

        # Update totals
        update_invoice_totals(invoice)

def update_invoice_totals(invoice):
    items = invoice.items.all()
    subtotal = sum(item.line_total for item in items)
    tax = subtotal * 0.075   # 7.5% VAT (modify this later)
    total = subtotal + tax

    invoice.subtotal = subtotal
    invoice.tax = tax
    invoice.total_amount = total
    invoice.save()
