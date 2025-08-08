from rest_framework import generics, permissions
from leads.models import Campaign
from leads.serializers import CampaignSerializer

class CampaignListCreateView(generics.ListCreateAPIView):
    queryset = Campaign.objects.all().order_by('-start_date')
    serializer_class = CampaignSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)


class CampaignRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Campaign.objects.all()
    serializer_class = CampaignSerializer
    permission_classes = [permissions.IsAuthenticated]
