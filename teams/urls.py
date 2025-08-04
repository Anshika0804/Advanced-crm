from django.urls import path
from .views import TeamCreateView, TeamListAPIView

urlpatterns = [
    path('create/', TeamCreateView.as_view(), name='team-create'),
    path('list/', TeamListAPIView.as_view(), name='team-list'),  # ✅ New endpoint
]
