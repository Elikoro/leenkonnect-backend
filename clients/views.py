from rest_framework import generics, permissions
from .models import Client, ClientContact, ClientAddress
from .serializers import (
    ClientSerializer,
    ClientContactSerializer,
    ClientAddressSerializer,
)


class ClientListCreateView(generics.ListCreateAPIView):
    serializer_class = ClientSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Client.objects.filter(organization=self.request.user.organization)

    def perform_create(self, serializer):
        serializer.save(organization=self.request.user.organization)


class ClientDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ClientSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Client.objects.filter(organization=self.request.user.organization)


class ClientContactCreateView(generics.CreateAPIView):
    serializer_class = ClientContactSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        client = Client.objects.get(
            id=self.kwargs["client_id"],
            organization=self.request.user.organization
        )
        serializer.save(client=client)


class ClientAddressCreateView(generics.CreateAPIView):
    serializer_class = ClientAddressSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        client = Client.objects.get(
            id=self.kwargs["client_id"],
            organization=self.request.user.organization
        )
        serializer.save(client=client)
from rest_framework import generics, permissions
from .models import Client, ClientContact, ClientAddress
from .serializers import (
    ClientSerializer,
    ClientContactSerializer,
    ClientAddressSerializer,
)


class ClientListCreateView(generics.ListCreateAPIView):
    serializer_class = ClientSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Client.objects.filter(organization=self.request.user.organization)

    def perform_create(self, serializer):
        serializer.save(organization=self.request.user.organization)


class ClientDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ClientSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Client.objects.filter(organization=self.request.user.organization)


class ClientContactCreateView(generics.CreateAPIView):
    serializer_class = ClientContactSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        client = Client.objects.get(
            id=self.kwargs["client_id"],
            organization=self.request.user.organization
        )
        serializer.save(client=client)


class ClientAddressCreateView(generics.CreateAPIView):
    serializer_class = ClientAddressSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        client = Client.objects.get(
            id=self.kwargs["client_id"],
            organization=self.request.user.organization
        )
        serializer.save(client=client)
