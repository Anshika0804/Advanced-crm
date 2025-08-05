from django.urls import path
from .views import (
    TeamListCreateView,
    TeamRetrieveUpdateDestroyView,
    TeamWithUsersListView
)

urlpatterns = [
    path('', TeamListCreateView.as_view(), name='team-list-create'),
    path('<int:pk>/', TeamRetrieveUpdateDestroyView.as_view(), name='team-detail'),
    path('with-users/', TeamWithUsersListView.as_view(), name='team-with-users'),
]
