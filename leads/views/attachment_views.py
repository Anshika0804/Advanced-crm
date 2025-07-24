from rest_framework import viewsets
from leads.models import Attachment
from leads.serializers import AttachmentSerializer

class AttachmentViewSet(viewsets.ModelViewSet):
    queryset = Attachment.objects.all()
    serializer_class = AttachmentSerializer
