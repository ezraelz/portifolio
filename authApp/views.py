from rest_framework import generics
from .models import User
from .serializers import UserSerializer, CustomTokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken 
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import authenticate, login,logout

class UserView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class ProfileView(APIView):
    def get(self, request):
        profile = User.objects.get(email=request.user)
        serializer = UserSerializer(profile)
        return Response(serializer.data, status=status.HTTP_200_OK)

class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer

class LoginView(APIView): 
    def post(self, request): 
        username = request.data.get('username') 
        password = request.data.get('password') 
        user = authenticate(username=username, password=password) 
        profile_image = None
        if hasattr(user, "profile_image") and user.profile_image:
            profile_image = request.build_absolute_uri(user.profile_image)

        if user is not None: 
            login(request, user) 
            refresh = RefreshToken.for_user(user) 
            return Response({
                "refresh": str(refresh),
                "access": str(refresh.access_token),
                "is_superuser": user.is_superuser,
        })
        else: return Response({'error': 'Invalid credentials'}, status=400)

