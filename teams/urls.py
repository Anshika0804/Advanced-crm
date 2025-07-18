from django.urls import path
from .views import TeamCreateView

urlpatterns = [
    path('create/', TeamCreateView.as_view(), name='team-create'),
]