# serializers.py
from rest_framework import serializers
from leads.models import Ticket, Lead
from users.models import CustomUser


class TicketSerializer(serializers.ModelSerializer):
    lead_name = serializers.CharField(source='lead.name', read_only=True)  # This is for display on frontend
    assigned_to = serializers.PrimaryKeyRelatedField(
        queryset=CustomUser.objects.all(),
        default=serializers.CurrentUserDefault()
    )

    class Meta:
        model = Ticket
        fields = [
            'id',
            'title',
            'description',
            'status',
            'priority',
            'lead',        
            'lead_name',   
            'assigned_to',
            'created_at',
            'updated_at',
        ]
        read_only_fields = ['created_at', 'updated_at']
