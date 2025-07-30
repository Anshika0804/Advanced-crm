from django.urls import path
from .views import RegisterView, UserProfileView, UpdateProfileView, LogoutView

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from .views import (
    RegisterView, UserProfileView, UpdateProfileView, LogoutView,
    ForgotPasswordView, ResetPasswordView, SendTestEmailView, UserListView
)
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('profile/', UserProfileView.as_view(), name='user_profile'),
    path('profile/update/', UpdateProfileView.as_view(), name='update-profile'),
    path('logout/', LogoutView.as_view(), name='logout'),
    
    path('forgot-password/', ForgotPasswordView.as_view(), name='forgot-password'),
    path("reset-password/<uidb64>/<token>/", ResetPasswordView.as_view(), name="reset-password"),
    path('send-test-email/', SendTestEmailView.as_view(), name='send-test-email'),

    path("list/", UserListView.as_view(), name="user-list"),

]