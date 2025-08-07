from django.db import models
from users.models import CustomUser
from teams.models import Team

class Ticket(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()

    STATUS_CHOICES = [
        ('open', 'Open'),
        ('in_progress', 'In Progress'),
        ('closed', 'Closed'),
    ]
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='open')

    PRIORITY_CHOICES = [
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('high', 'High'),
    ]
    priority = models.CharField(max_length=50, choices=PRIORITY_CHOICES, default='medium')

    lead = models.ForeignKey("leads.Lead", on_delete=models.CASCADE, default=1)
    assigned_to = models.ForeignKey(CustomUser, null=True, blank=True, on_delete=models.SET_NULL)
    team = models.ForeignKey(Team, null=True, blank=True, on_delete=models.SET_NULL)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
