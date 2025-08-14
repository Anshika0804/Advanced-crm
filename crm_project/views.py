from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.conf import settings
from leads.models import Lead
from users.models import CustomUser
from teams.models import Team
import redis

# @api_view(['GET'])
# @permission_classes([IsAuthenticated])
# def leads_count(request):
#     redis_client = settings.REDIS_CLIENT
#     redis_key = "leadsCount"

#     cached_count = redis_client.get(redis_key)
#     if cached_count is not None:
#         return Response({'count': int(cached_count)})

#     count = Lead.objects.count()

#     # Store in Redis with TTL 1hr
#     redis_client.set(redis_key, count, ex=60*60)

#     return Response({'count': count})

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def leads_count(request):
    redis_client = settings.REDIS_CLIENT
    cached_count = redis_client.get("leadsCount")

    return Response({'count': int(cached_count) if cached_count else 0})


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def users_count(request):
    redis_client = settings.REDIS_CLIENT
    cached_count = redis_client.get("usersCount")

    return Response({'count': int(cached_count) if cached_count else 0})

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def teams_count(request):
    redis_client = settings.REDIS_CLIENT
    cached_count = redis_client.get("teamsCount")

    return Response({'count': int(cached_count) if cached_count else 0})




