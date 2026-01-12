from django.urls import path
from .views import UserView, CustomTokenObtainPairView, LoginView, ProfileView
from rest_framework_simplejwt.views import TokenRefreshView


urlpatterns = [
    path('users', UserView.as_view(), name='users'),
    path('token/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('login/', LoginView.as_view(), name='login'),
    path('profile/', ProfileView.as_view(), name='profile'),

]

