from django.urls import path
from leads.views.attachment_views import (TicketAttachmentsListView, AttachmentRetrieveUpdateDestroyView
)

urlpatterns = [
    # List all notes for a given lead, or upload a new attachement
    path('attachment/', TicketAttachmentsListView.as_view(), name='attachment-list-create'),

    # Retrieve, update, or delete a specific attachment
    path('attachment/<int:pk>/', AttachmentRetrieveUpdateDestroyView.as_view(), name='attachment-detail-update-delete'),
]