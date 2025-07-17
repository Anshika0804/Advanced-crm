from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import Response
from .serializers import RegisterSerializer, LeadSerializer
from .models import CustomUser, Lead
from rest_framework.permissions import AllowAny

# Create your views here.
class RegisterView(generics.CreateAPIView):
    # queryset = CustomUser.objects.all()
    serializer_class = RegisterSerializer
    # permission_classes = [AllowAny]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user_data = serializer.save()
        return Response(user_data, status=status.HTTP_201_CREATED)
    

class LeadListCreateView(generics.ListCreateAPIView):
    queryset = Lead.objects.all()
    serializer_class = LeadSerializer

class LeadUpdateRetrieveDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Lead.objects.all()
    serializer_class = LeadSerializer