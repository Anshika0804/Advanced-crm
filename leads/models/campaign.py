from django.db import models
from teams.models import Team
from users.models import CustomUser

class Campaign(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    start_date = models.DateField()
    end_date = models.DateField()

    created_by = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True)
    team = models.ForeignKey(Team, on_delete=models.SET_NULL, null=True, blank=True)
    leads = models.ManyToManyField("leads.Lead", blank=True)

    STATUS_CHOICES = [
        ('draft', 'Draft'),
        ('running', 'Running'),
        ('completed', 'Completed'),
    ]
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='draft')

    def __str__(self):
        return self.name
