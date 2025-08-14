from celery import shared_task
from django.conf import settings
from leads.models import Lead
from users.models import CustomUser
from teams.models import Team

REDIS_TTL = 10 * 60

@shared_task
def update_leads_count():
    redis_client = settings.REDIS_CLIENT
    count = Lead.objects.count()
    redis_client.set("leadsCount", count, ex=REDIS_TTL)
    return count

@shared_task
def update_users_count():
    redis_client = settings.REDIS_CLIENT
    count = CustomUser.objects.count()
    redis_client.set("usersCount", count, ex=REDIS_TTL)
    return count

@shared_task
def update_teams_count():
    redis_client = settings.REDIS_CLIENT
    count = Team.objects.count()
    redis_client.set("teamsCount", count, ex=REDIS_TTL)
    return count
