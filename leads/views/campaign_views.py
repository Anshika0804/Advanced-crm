from rest_framework import generics, permissions
from leads.models import Campaign
from leads.serializers import CampaignSerializer
from permissions.permissions import (
    IsAgentOrAbove,
    IsTeamLeadOrAbove,
    IsManagerOrAdmin
)

class CampaignListCreateView(generics.ListCreateAPIView):
    queryset = Campaign.objects.all().order_by('-start_date')
    serializer_class = CampaignSerializer
    permission_classes = [IsManagerOrAdmin]

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)


class CampaignRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Campaign.objects.all()
    serializer_class = CampaignSerializer
    permission_classes = [IsManagerOrAdmin]
