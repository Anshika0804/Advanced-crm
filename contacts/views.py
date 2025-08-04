from rest_framework import generics
from .models import Contact
from .serializers import ContactSerializer

# Get, Update, or Delete a single contact by ID
class ContactDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer


class ContactCreateView(generics.CreateAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
