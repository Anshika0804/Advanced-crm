from .models import Lead
from rest_framework import serializers
from .models import Lead
from django.contrib.auth.password_validation import validate_password
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated


class LeadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lead
        fields = '__all__'

class LeadListCreateView(generics.ListCreateAPIView):
    serializer_class = LeadSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Lead.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
