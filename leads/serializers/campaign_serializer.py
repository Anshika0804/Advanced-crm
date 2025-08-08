from rest_framework import serializers
from leads.models import Campaign, Lead
from users.models import CustomUser
from teams.models import Team

class CampaignSerializer(serializers.ModelSerializer):
    created_by_name = serializers.CharField(source='created_by.name', read_only=True)
    team_name = serializers.CharField(source='team.name', read_only=True)
    leads_count = serializers.IntegerField(source='leads.count', read_only=True)

    class Meta:
        model = Campaign
        fields = [
            'id',
            'name',
            'description',
            'start_date',
            'end_date',
            'created_by',
            'created_by_name',
            'team',
            'team_name',
            'leads',
            'leads_count',
            'status',
        ]
        read_only_fields = ['created_by', 'created_by_name', 'leads_count']

    def create(self, validated_data):
        # Assign current user as created_by automatically
        validated_data['created_by'] = self.context['request'].user
        return super().create(validated_data)
