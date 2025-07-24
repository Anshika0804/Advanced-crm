from django.shortcuts import render
from rest_framework import viewsets, permissions
from .models import Contact
from .serializers import ContactSerializer

# Create your views here.
class ContactViewSet(viewsets.ModelViewSet):
    serializer_class = ContactSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Contact.objects.filter(created_by=self.request.user)
    
    def perform_create(self,serializer):
        serializer.save(created_by=self.request.user)

