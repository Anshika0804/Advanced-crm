from rest_framework import generics, permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from django.core.exceptions import ValidationError

from .models import Team
from .serializers import TeamSerializer, TeamWithUsersSerializer
from permissions.permissions import IsAgentOrAbove, IsTeamLeadOrAbove
from rest_framework.permissions import IsAuthenticated

# List and Create View (similar to LeadListCreateView)
class TeamListCreateView(generics.ListCreateAPIView):
    serializer_class = TeamSerializer
    permission_classes = [IsTeamLeadOrAbove]

    def get_queryset(self):
        user = self.request.user

        if user.role == "admin":
            return Team.objects.all()
        elif user.role in ["manager", "team_lead"]:
            return Team.objects.filter(assigned_to=user)
        elif user.role == "agent":
            return Team.objects.filter(users=user)
        return Team.objects.none()

    def perform_create(self, serializer):
        user = self.request.user
        if not user.role:
            raise ValidationError("User has no role assigned.")
        serializer.save(assigned_to=user)


# Retrieve/Update/Delete View
class TeamRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TeamSerializer
    permission_classes = [IsTeamLeadOrAbove]

    def get_queryset(self):
        user = self.request.user

        if user.role == "admin":
            return Team.objects.all()
        elif user.role in ["manager", "team_lead"]:
            return Team.objects.filter(assigned_to=user)
        elif user.role == "agent":
            return Team.objects.filter(users=user)
        return Team.objects.none()


# Extended list (with users)
class TeamWithUsersListView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user

        if user.role == "admin":
            teams = Team.objects.all()
        elif user.role in ["manager", "team_lead"]:
            teams = Team.objects.filter(assigned_to=user)
        elif user.role == "agent":
            teams = Team.objects.filter(users=user)
        else:
            teams = Team.objects.none()

        serializer = TeamWithUsersSerializer(teams, many=True)
        return Response(serializer.data)
