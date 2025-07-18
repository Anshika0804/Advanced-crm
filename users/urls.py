from django.urls import path
from .views import RegisterView, ManagerOnlyView, UserProfileView, UpdateProfileView, LogoutView

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('manager-only/', ManagerOnlyView.as_view(), name='manager-only'),
    path('profile/', UserProfileView.as_view(), name='user_profile'),
    path('profile/update/', UpdateProfileView.as_view(), name='update-profile'),
    path('logout/', LogoutView.as_view(), name='logout'),
]
