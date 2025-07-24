from rest_framework import viewsets
from leads.models import Campaign
from leads.serializers import CampaignSerializer

class CampaignViewSet(viewsets.ModelViewSet):
    queryset = Campaign.objects.all()
    serializer_class = CampaignSerializer
