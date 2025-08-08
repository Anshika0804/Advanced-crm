from django.urls import path
from leads.views import TicketAttachmentsListView

urlpatterns = [
    path('tickets/<int:ticket_id>/attachments/', TicketAttachmentsListView.as_view(), name='ticket-attachments'),
]
