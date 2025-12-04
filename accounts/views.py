from rest_framework import status, generics
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from .serializers import RegisterSerializer, LoginSerializer, UserSerializer
from .permissions import IsAdmin, AllowRoles, IsTechnician, IsClient, IsManager

from .models import User


class RegisterView(generics.CreateAPIView):
    serializer_class = RegisterSerializer


class LoginView(APIView):
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = serializer.validated_data["user"]

        refresh = RefreshToken.for_user(user)

        response = Response({
            "user": UserSerializer(user).data
        })

        # Set HttpOnly cookies for access and refresh tokens
        access_token = str(refresh.access_token)
        refresh_token = str(refresh)

        # access cookie (short lived)
        response.set_cookie(
            key='access',
            value=access_token,
            httponly=True,
            secure=False,  # set True in production
            samesite='Lax',
        )

        # refresh cookie (longer lived)
        response.set_cookie(
            key='refresh',
            value=refresh_token,
            httponly=True,
            secure=False,  # set True in production
            samesite='Lax',
        )

        return response


class RefreshTokenView(TokenRefreshView):
    pass


class LogoutView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        try:
            refresh_token = request.data["refresh"]
            token = RefreshToken(refresh_token)
            token.blacklist()
            response = Response({"message": "Logout successful"}, status=200)
            # clear cookies
            response.delete_cookie('access')
            response.delete_cookie('refresh')
            return response
        except:
            return Response({"error": "Invalid token"}, status=400)


class UserProfileView(generics.RetrieveAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = UserSerializer

    def get_object(self):
        return self.request.user
    
class AdminDashboard(APIView):
    permission_classes = [IsAdmin]

    def get(self, request):
        return Response({"message": "Welcome Admin!"})


class ManagerDashboard(APIView):
    permission_classes = [AllowRoles]
    allowed_roles = ['admin', 'manager']

    def get(self, request):
        return Response({"message": "Manager/Admin Access"})


class TechnicianTaskView(APIView):
    permission_classes = [IsTechnician]

    def get(self, request):
        return Response({"message": "Technician Portal"})


class ClientDashboard(APIView):
    permission_classes = [IsClient]

    def get(self, request):
        return Response({"message": "Client Dashboard"})
