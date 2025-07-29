from rest_framework import serializers
from leads.models import Lead  
from .ticket_serializer import TicketSerializer
from .note_serializer import NoteSerializer
from .attachment_serializer import AttachmentSerializer
from .campaign_serializer import CampaignSerializer

__all__ = [
    "TicketSerializer",
    "LeadSerializer",
    "NoteSerializer",
    "AttachmentSerializer",
    "CampaignSerializer",
]

class LeadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lead
        fields = '__all__'

    def get_user(self, obj):
        return obj.user.email if obj.user else None

    def get_assigned_to(self, obj):
        return obj.assigned_to.email if obj.assigned_to else None


# FRONTEND.....

# leads/serializers.py

from rest_framework import serializers
from leads.models import Lead
from users.models import CustomUser  # adjust if your user model is named differently

class LeadExtendedSerializer(serializers.ModelSerializer):
    assigned_by_name = serializers.SerializerMethodField()
    assigned_to_name = serializers.SerializerMethodField()

    class Meta:
        model = Lead
        fields = [
            "id", "name", "email", "phone_number", "status", 
            "created_at", "updated_at", "assigned_by_name", "assigned_to_name"
        ]

    def get_assigned_by_name(self, obj):
        return obj.user.name if obj.user and hasattr(obj.user, "name") else obj.user.username if obj.user else None

    def get_assigned_to_name(self, obj):
        return obj.assigned_to.name if obj.assigned_to and hasattr(obj.assigned_to, "name") else obj.assigned_to.username if obj.assigned_to else None

