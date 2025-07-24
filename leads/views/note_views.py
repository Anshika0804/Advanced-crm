from rest_framework import viewsets
from leads.models import Note
from leads.serializers import NoteSerializer

class NoteViewSet(viewsets.ModelViewSet):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
