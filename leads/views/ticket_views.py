from rest_framework import viewsets
from leads.models import Ticket
from leads.serializers import TicketSerializer

class TicketViewSet(viewsets.ModelViewSet):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer
