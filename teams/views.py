from django.shortcuts import render
from rest_framework import generics, permissions
from .models import Team
from .serializers import TeamSerializer

# Create your views here.
class TeamCreateView(generics.CreateAPIView):
    serializer_class = TeamSerializer
    permission_classes = [permissions.IsAdminUser]

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

