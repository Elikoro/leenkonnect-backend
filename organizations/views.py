from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import Organization, StaffProfile, TechnicianProfile, ClientProfile
from .serializers import (
    OrganizationSerializer, StaffProfileSerializer,
    TechnicianProfileSerializer, ClientProfileSerializer
)
from .permissions import IsOrganizationAdmin


class OrganizationListCreateView(generics.ListCreateAPIView):
    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializer
    permission_classes = [IsAuthenticated, IsOrganizationAdmin]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class OrganizationDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializer
    permission_classes = [IsAuthenticated, IsOrganizationAdmin]


class StaffProfileCreateView(generics.CreateAPIView):
    queryset = StaffProfile.objects.all()
    serializer_class = StaffProfileSerializer
    permission_classes = [IsAuthenticated, IsOrganizationAdmin]


class TechnicianProfileCreateView(generics.CreateAPIView):
    queryset = TechnicianProfile.objects.all()
    serializer_class = TechnicianProfileSerializer
    permission_classes = [IsAuthenticated, IsOrganizationAdmin]


class ClientProfileCreateView(generics.CreateAPIView):
    queryset = ClientProfile.objects.all()
    serializer_class = ClientProfileSerializer
    permission_classes = [IsAuthenticated, IsOrganizationAdmin]

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)
