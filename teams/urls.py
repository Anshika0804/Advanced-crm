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


from .views import assign_users_to_team, remove_users_from_team

urlpatterns += [
    path('<int:team_id>/assign-users/', assign_users_to_team, name='assign-users-to-team'),
    path('<int:team_id>/remove-users/', remove_users_from_team, name='remove-users-from-team'),
]