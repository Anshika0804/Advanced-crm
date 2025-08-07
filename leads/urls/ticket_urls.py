from django.urls import path
from leads.views.ticket_views import (
    TicketListCreateAPIView,
    TicketRetrieveUpdateDestroyAPIView,
)

urlpatterns = [
    path('tickets/', TicketListCreateAPIView.as_view(), name='ticket-list-create'),
    path('tickets/<int:pk>/', TicketRetrieveUpdateDestroyAPIView.as_view(), name='ticket-detail'),
]
