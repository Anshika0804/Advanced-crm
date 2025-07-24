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
