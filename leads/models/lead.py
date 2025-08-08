from django.db import models
from users.models import CustomUser
from teams.models import Team

# Create your models here.
class Lead(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    STATUS_CHOICES = [
        ('New', 'New'), 
        ('Contacted', 'Contacted'),
        ('Qualified', 'Qualified'),
        ('Lost', 'Lost')
    ]
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='New')

    assigned_to = models.ForeignKey(
        CustomUser,
        related_name='assigned_leads',
        null=True,
        blank=True,
        on_delete=models.SET_NULL
    )

    team = models.ForeignKey(
        Team,
        null=True,
        blank=True,
        on_delete=models.SET_NULL
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        if not self.team:
            if self.assigned_to and self.assigned_to.team:
                self.team = self.assigned_to.team
            elif self.user and self.user.team:
                self.team = self.user.team
        super().save(*args, **kwargs)


    
