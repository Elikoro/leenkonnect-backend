from django.urls import path
from .views import (
    ClientListCreateView,
    ClientDetailView,
    ClientContactCreateView,
    ClientAddressCreateView
)

urlpatterns = [
    path('', ClientListCreateView.as_view(), name='clients'),
    path('<int:pk>/', ClientDetailView.as_view(), name='client-detail'),

    # Contact endpoints
    path('<int:client_id>/contacts/', ClientContactCreateView.as_view(), name='client-contact'),

    # Address endpoints
    path('<int:client_id>/addresses/', ClientAddressCreateView.as_view(), name='client-address'),
]

