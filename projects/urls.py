from django.urls import path
from .views import (
    ProjectListCreateView,
    ProjectDetailView,
    ProjectUpdateCreateView,
    ProjectFileCreateView
)

urlpatterns = [
    path('', ProjectListCreateView.as_view(), name='projects'),
    path('<int:pk>/', ProjectDetailView.as_view(), name='project-detail'),
    path('<int:project_id>/updates/', ProjectUpdateCreateView.as_view(), name='project-updates'),
    path('<int:project_id>/files/', ProjectFileCreateView.as_view(), name='project-files'),
]
