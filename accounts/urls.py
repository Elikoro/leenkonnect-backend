from django.urls import path
from .views import (
    RegisterView, LoginView, LogoutView, RefreshTokenView,
    UserProfileView,
    AdminDashboard, ManagerDashboard,
    TechnicianTaskView, ClientDashboard
)

urlpatterns = [
    path('register/', RegisterView.as_view()),
    path('login/', LoginView.as_view()),
    path('logout/', LogoutView.as_view()),
    path('refresh/', RefreshTokenView.as_view()),
    path('me/', UserProfileView.as_view()),

    # RBAC Test URLs
    path('admin/dashboard/', AdminDashboard.as_view()),
    path('manager/dashboard/', ManagerDashboard.as_view()),
    path('technician/tasks/', TechnicianTaskView.as_view()),
    path('client/dashboard/', ClientDashboard.as_view()),
]
