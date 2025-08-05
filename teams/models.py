from django.db import models
from django.conf import settings

class Team(models.Model):
    name = models.CharField(max_length=100, unique=True)
    assigned_to = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name='assigned_teams',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        limit_choices_to={'role__in': ['admin', 'manager', 'team_lead']}
    )
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    def member_count(self):
        return self.users.count()

    def save(self, *args, **kwargs):
        # Optional: logic similar to Lead's save
        if not self.assigned_to and self.users.exists():
            first_user = self.users.first()
            if first_user and first_user.role in ['admin', 'manager', 'team_lead']:
                self.assigned_to = first_user
        super().save(*args, **kwargs)
