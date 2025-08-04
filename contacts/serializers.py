# contacts/serializers.py
from rest_framework import serializers
from contacts.models import Contact

# contacts/serializers.py

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ['id', 'name', 'email', 'phone_number', 'created_at', 'lead']
        read_only_fields = ['lead', 'created_at']
