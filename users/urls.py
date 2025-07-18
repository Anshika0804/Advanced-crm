from django.urls import path
from .views import RegisterView, LeadListCreateView, LeadUpdateRetrieveDestroyView, ManagerOnlyView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('leads/', LeadListCreateView.as_view(), name='lead-list-create'),
    path('leads/<int:pk>/', LeadUpdateRetrieveDestroyView.as_view(), name='lead-detail'),
    path('manager-only/', ManagerOnlyView.as_view(), name='manager-only'),
]
