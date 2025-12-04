from rest_framework import generics, permissions
from .models import Ticket, TicketComment
from .serializers import TicketSerializer, TicketCommentSerializer


class TicketListCreateView(generics.ListCreateAPIView):
    serializer_class = TicketSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Ticket.objects.filter(organization=self.request.user.organization)

    def perform_create(self, serializer):
        serializer.save(
            organization=self.request.user.organization,
            created_by=self.request.user
        )


class TicketDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TicketSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Ticket.objects.filter(organization=self.request.user.organization)


class TicketCommentCreateView(generics.CreateAPIView):
    serializer_class = TicketCommentSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        ticket_id = self.kwargs["ticket_id"]
        ticket = Ticket.objects.get(id=ticket_id, organization=self.request.user.organization)
        
        serializer.save(
            ticket=ticket,
            author=self.request.user
        )
