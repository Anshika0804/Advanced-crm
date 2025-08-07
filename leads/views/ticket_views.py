# views.py
from rest_framework import generics
from leads.models import Ticket
from leads.serializers import TicketSerializer
from rest_framework.permissions import IsAuthenticated

class TicketListCreateAPIView(generics.ListCreateAPIView):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer

    def perform_create(self, serializer):
        serializer.save(assigned_to=self.request.user)


class TicketRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer
