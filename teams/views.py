from rest_framework import generics, status, permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from django.core.exceptions import ValidationError

from .models import Team
from .serializers import TeamSerializer, TeamWithUsersSerializer
from permissions.permissions import IsAgentOrAbove, IsTeamLeadOrAbove
from rest_framework.permissions import IsAuthenticated

from rest_framework.decorators import api_view, permission_classes
from users.models import CustomUser

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
        if not self.request.user.role:
            raise ValidationError("User has no role assigned.")

        if not serializer.validated_data.get("assigned_to"):
            serializer.save(assigned_to=self.request.user)
        else:
            serializer.save()


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


# API view to update users' team
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def assign_users_to_team(request, team_id):
    try:
        team = Team.objects.get(id=team_id)
    except Team.DoesNotExist:
        return Response({"detail": "Team not found."}, status=status.HTTP_404_NOT_FOUND)

    user_ids = request.data.get("user_ids", [])

    if not isinstance(user_ids, list):
        return Response({"detail": "user_ids must be a list."}, status=status.HTTP_400_BAD_REQUEST)

    users = CustomUser.objects.filter(id__in=user_ids)

    # Assign each user to the team
    users.update(team=team)

    return Response({"detail": "Users assigned to team successfully."}, status=status.HTTP_200_OK)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def remove_users_from_team(request, team_id):
    try:
        team = Team.objects.get(id=team_id)
    except Team.DoesNotExist:
        return Response({"detail": "Team not found."}, status=status.HTTP_404_NOT_FOUND)

    user_ids = request.data.get("user_ids", [])

    if not isinstance(user_ids, list):
        return Response({"detail": "user_ids must be a list."}, status=status.HTTP_400_BAD_REQUEST)

    users = CustomUser.objects.filter(id__in=user_ids, team=team)

    # Remove users from the team
    users.update(team=None)

    return Response({"detail": "Users removed from team successfully."}, status=status.HTTP_200_OK)
