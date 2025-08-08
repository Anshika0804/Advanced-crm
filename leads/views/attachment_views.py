
from leads.serializers import AttachmentSerializer
from rest_framework.decorators import api_view
from leads.models import Attachment
from rest_framework import generics

class TicketAttachmentsListView(generics.ListCreateAPIView):
    serializer_class = AttachmentSerializer

    def get_queryset(self):
        ticket_id = self.kwargs['ticket_id']
        return Attachment.objects.filter(ticket_id=ticket_id).order_by('-uploaded_at')

    def perform_create(self, serializer):
        serializer.save(
            uploaded_by=self.request.user,
            ticket_id=self.kwargs['ticket_id']
        )
