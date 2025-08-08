from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from leads.models import Lead
from users.models import CustomUser
from teams.models import Team

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def leads_count(request):
    count = Lead.objects.count()
    return Response({'count': count})

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def users_count(request):
    count = CustomUser.objects.count()
    return Response({'count': count})

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def teams_count(request):
    count = Team.objects.count()
    return Response({'count': count})
