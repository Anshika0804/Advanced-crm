from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken, TokenError
from rest_framework.views import APIView
from .serializers import RegisterSerializer, UserProfileSerializer, UpdateProfileSerializer
# from .models import CustomUser
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
    
    
class LogoutView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request):
        try:
            refresh_token = request.data["refresh"]
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response({"detail": "Logout successful."}, status=status.HTTP_205_RESET_CONTENT)
        except KeyError:
            return Response({"error": "Refresh token not provided"}, status=status.HTTP_400_BAD_REQUEST)
        except TokenError:
            return Response({"error": "Invalid token"}, status=status.HTTP_400_BAD_REQUEST)

class ManagerOnlyView(APIView):
    permission_classes = [IsAuthenticated, IsManager]
    def get(self, request):        
        return Response({"message": "Hello Manager!"})
    



    