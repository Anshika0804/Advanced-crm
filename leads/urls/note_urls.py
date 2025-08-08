# leads/urls/note_urls.py
from django.urls import path
from leads.views.note_views import (
    TicketNotesListView,
    NoteRetrieveUpdateDestroyView
)

urlpatterns = [
    # List all notes for a given lead, or create a new note
    path('notes/', TicketNotesListView.as_view(), name='note-list-create'),

    # Retrieve, update, or delete a specific note
    path('notes/<int:pk>/', NoteRetrieveUpdateDestroyView.as_view(), name='note-detail-update-delete'),
]
