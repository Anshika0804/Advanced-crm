from rest_framework import generics
from leads.models import Note, Ticket
from leads.serializers import NoteSerializer
from rest_framework.exceptions import ValidationError
from permissions.permissions import (
    IsAgentOrAbove,
    IsTeamLeadOrAbove,
)


# List + Create notes for a specific ticket
class TicketNotesListView(generics.ListCreateAPIView):
    serializer_class = NoteSerializer
    permission_classes = [IsTeamLeadOrAbove]

    def get_queryset(self):
        ticket_id = self.request.query_params.get('ticket_id')
        if not ticket_id:
            return Note.objects.none()
        return Note.objects.filter(ticket_id=ticket_id).order_by('-created_at')

    def perform_create(self, serializer):
        ticket = serializer.validated_data.get('ticket')
        if not ticket:
            raise ValidationError("Ticket must be provided in request data")
        lead = ticket.lead if hasattr(ticket, 'lead') else None

        serializer.save(
            created_by=self.request.user,
            lead=lead
        )


# Retrieve, Update, Delete a specific note
class NoteRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
