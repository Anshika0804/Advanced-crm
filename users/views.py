from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken, TokenError
from rest_framework.views import APIView
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.utils.encoding import force_bytes, force_str
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.core.mail import send_mail
from django.contrib.auth import get_user_model

from django.core.mail import send_mail
from django.http import JsonResponse
from django.views import View
from .models import CustomUser
from .serializers import UserSerializer


from .serializers import RegisterSerializer, UserProfileSerializer, UpdateProfileSerializer
from permissions.permissions import IsManagerOrAdmin

# Create your views here.


class RegisterView(generics.CreateAPIView):
    serializer_class = RegisterSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()

        # Assign role if provided
        role = request.data.get('role')
        if role in ['manager', 'admin', 'agent', 'team_lead', 'custom']:
            user.role = role
            user.save()

        # Generate tokens
        refresh = RefreshToken.for_user(user)
        token_data = {
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        }

        return Response({
            "email": user.email,
            "name": user.name,
            "role": user.role,
            "token": token_data,
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

class ProtectedRoleView(APIView):
    permission_classes = [IsAuthenticated, IsManagerOrAdmin]

    def get(self, request):
        return Response({"message": f"Hello {request.user.role.title()}!"})


class ForgotPasswordView(APIView):
    def post(self, request):
        email = request.data.get("email")
        if not email :
            return Response({"error": "Email is required."}, status=status.HTTP_400_BAD_REQUEST)
        
        User = get_user_model()
        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            return Response({"error": "User with this email does not exist."}, status=status.HTTP_404_NOT_FOUND)
        
        uid = urlsafe_base64_encode(force_bytes(user.pk))
        token = PasswordResetTokenGenerator().make_token(user)
        reset_link = f"http://localhost:3000/reset-password/{uid}/{token}/"

        send_mail(
            "Reset Your Password",
            f"Click the link to reset your password: {reset_link}",
            "noreply@crm.com",
            [email],
            fail_silently=False,
        )

        return Response({"message": "Password reset link sent to your email."}, status=status.HTTP_200_OK)


class ResetPasswordView(APIView):
    def post(self, request, uidb64, token):
        password = request.data.get("password")
        if not password:
            return Response({"error": "Password is required."}, status=status.HTTP_400_BAD_REQUEST)

        User = get_user_model()
        try:
            uid = force_str(urlsafe_base64_decode(uidb64))
            user = User.objects.get(pk=uid)
        except (TypeError, ValueError, OverflowError, User.DoesNotExist):
            return Response({"error": "Invalid reset link."}, status=status.HTTP_400_BAD_REQUEST)

        if not PasswordResetTokenGenerator().check_token(user, token):
            return Response({"error": "Invalid or expired token."}, status=status.HTTP_400_BAD_REQUEST)

        user.set_password(password)
        user.save()
        return Response({"message": "Password reset successful."}, status=status.HTTP_200_OK)


class SendTestEmailView(View):
    def get(self, request):
        subject = 'Test Email from Django'
        message = 'This is a test email sent from your Django project using Gmail SMTP.'
        from_email = 'anshikacoder10@gmail.com'  # Replace with your actual email
        recipient_list = ['skrcoder07@gmail.com']  # Replace with the email you want to receive the test on

        try:
            send_mail(subject, message, from_email, recipient_list)
            return JsonResponse({'success': 'Email sent successfully'})
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
        



from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import get_user_model
from users.serializers import UserSerializer  # make sure this serializer exists

User = get_user_model()

class UserListView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)
