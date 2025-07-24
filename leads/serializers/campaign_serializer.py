from rest_framework import serializers
from leads.models import Campaign

class CampaignSerializer(serializers.ModelSerializer):
    class Meta:
        model = Campaign
        fields = '__all__'
