from rest_framework import generics, permissions
from .models import Project, ProjectUpdate, ProjectFile
from .serializers import (
    ProjectSerializer,
    ProjectUpdateSerializer,
    ProjectFileSerializer
)


class ProjectListCreateView(generics.ListCreateAPIView):
    serializer_class = ProjectSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Project.objects.filter(organization=self.request.user.organization)

    def perform_create(self, serializer):
        serializer.save(
            organization=self.request.user.organization,
            created_by=self.request.user
        )

class ProjectDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ProjectSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Project.objects.filter(organization=self.request.user.organization)

class ProjectUpdateCreateView(generics.CreateAPIView):
    serializer_class = ProjectUpdateSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        project_id = self.kwargs['project_id']
        project = Project.objects.get(
            id=project_id,
            organization=self.request.user.organization
        )
        serializer.save(
            project=project,
            author=self.request.user
        )

class ProjectFileCreateView(generics.CreateAPIView):
    serializer_class = ProjectFileSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        project_id = self.kwargs['project_id']
        project = Project.objects.get(
            id=project_id,
            organization=self.request.user.organization
        )
        serializer.save(
            project=project,
            uploaded_by=self.request.user
        )
