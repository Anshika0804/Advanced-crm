from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.views import APIView
from .serializers import RegisterSerializer, LeadSerializer, UserProfileSerializer, UpdateProfileSerializer
from .models import CustomUser, Lead
from .permissions import IsManager

# Create your views here.
class RegisterView(generics.CreateAPIView):
    # queryset = CustomUser.objects.all()
    serializer_class = RegisterSerializer
    # permission_classes = [AllowAny]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()

        if request.data.get('is_manager') == True or request.data.get('is_manager') == 'true':
            try:
                group = Group.objects.get(name='Manager')
                user.groups.add(group)
            except Group.DoesNotExist:
                return Response({'error': 'Manager Group does not exist'}, status=status.HTTP_400_BAD_REQUEST)

        return Response({
            "email": user.email,
            "name": user.name,
            "message": "User registered successfully"
        }, status=status.HTTP_201_CREATED)

    
class UserProfileView(generics.RetrieveAPIView):
    serializer_class = UserProfileSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user
    
class UpdateProfileView(generics.UpdateAPIView):
    serializer_class = UpdateProfileSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user
    
    def update(self, request, *args, **kwargs):
        print("Update request data:", request.data)
        return super().update(request, *args, **kwargs)

class LeadListCreateView(generics.ListCreateAPIView):
    queryset = Lead.objects.all()
    serializer_class = LeadSerializer
    permission_classes = [IsAuthenticated]

class LeadUpdateRetrieveDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Lead.objects.all()
    serializer_class = LeadSerializer
    permission_classes = [IsAuthenticated]


class ManagerOnlyView(APIView):
    permission_classes = [IsAuthenticated, IsManager]
    def get(self, request):        
        return Response({"message": "Hello Manager!"})
    



    