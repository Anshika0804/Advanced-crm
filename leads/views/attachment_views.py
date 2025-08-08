
from leads.serializers import AttachmentSerializer
from rest_framework.decorators import api_view
from leads.models import Attachment
from rest_framework.exceptions import ValidationError
from rest_framework import generics

class TicketAttachmentsListView(generics.ListCreateAPIView):
    serializer_class = AttachmentSerializer

    def get_queryset(self):
        ticket_id = self.request.query_params.get('ticket_id')
        if not ticket_id:
            return Attachment.objects.none()
        return Attachment.objects.filter(ticket_id=ticket_id).order_by('-uploaded_at')
    
    def perform_create(self, serializer):
        ticket = serializer.validated_data.get('ticket')
        if not ticket:
            raise ValidationError("Ticket must be provided in request data")
        lead = ticket.lead if hasattr(ticket, 'lead') else None

        serializer.save(
            uploaded_by=self.request.user,
            lead=lead
        )


class AttachmentRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Attachment.objects.all()
    serializer_class = AttachmentSerializer
