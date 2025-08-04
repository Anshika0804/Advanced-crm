from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from leads.serializers import LeadSerializer
from leads.models import Lead

from permissions.permissions import (
    IsAgentOrAbove,
    IsTeamLeadOrAbove,
)
from django.core.exceptions import ValidationError
from rest_framework.views import APIView
from rest_framework.response import Response

# Create/List View
class LeadListCreateView(generics.ListCreateAPIView):
    serializer_class = LeadSerializer
    permission_classes = [IsAgentOrAbove]

    def get_queryset(self):
        user = self.request.user
        print("User:", user)
        print("Role:", user.role)

        if user.role == "admin":
            return Lead.objects.all()
        elif user.role in ["manager", "team_lead"]:
            return Lead.objects.filter(team=user.team)
        elif user.role == "agent":
            return Lead.objects.filter(user=user)
        return Lead.objects.none()

    def perform_create(self, serializer):
        user = self.request.user
        if not user.role:
            raise ValidationError("User has no role assigned.")
        serializer.save(user=user)  # ✅ Removed team


# Detail View (Retrieve/Update/Delete)
class LeadUpdateRetrieveDestroyView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = LeadSerializer
    permission_classes = [IsTeamLeadOrAbove]

    def get_queryset(self):
        user = self.request.user
        print("User (detail view):", user)
        print("Role (detail view):", user.role)

        if user.role == "agent":
            return Lead.objects.filter(user=user)
        elif user.role in ["manager", "admin", "team_lead"]:
            return Lead.objects.all()
        return Lead.objects.none()


# Optional: List View used for extended table view on frontend (same serializer now)
class LeadExtendedListView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        if user.role == "admin":
            leads = Lead.objects.all()
        elif user.role in ["manager", "team_lead"]:
            leads = Lead.objects.filter(team=user.team)
        elif user.role == "agent":
            leads = Lead.objects.filter(user=user)
        else:
            leads = Lead.objects.none()

        serializer = LeadSerializer(leads, many=True)
        return Response(serializer.data)


from leads.serializers import LeadWithContactsSerializer

class LeadWithContactsListView(generics.ListAPIView):
    queryset = Lead.objects.all().prefetch_related('contacts')
    serializer_class = LeadWithContactsSerializer
