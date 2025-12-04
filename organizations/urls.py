from django.urls import path
from .views import (
    OrganizationListCreateView, OrganizationDetailView,
    StaffProfileCreateView, TechnicianProfileCreateView,
    ClientProfileCreateView
)

urlpatterns = [
    path('organizations/', OrganizationListCreateView.as_view(), name='org-list'),
    path('organizations/<int:pk>/', OrganizationDetailView.as_view(), name='org-detail'),

    path('staff/add/', StaffProfileCreateView.as_view(), name='add-staff'),
    path('technicians/add/', TechnicianProfileCreateView.as_view(), name='add-technician'),
    path('clients/add/', ClientProfileCreateView.as_view(), name='add-client'),
]
