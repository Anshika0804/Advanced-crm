from django.db import models
from users.models import CustomUser
from django.conf import settings
from .ticket import Ticket
from .attachment import Attachment
from .campaign import Campaign
from .note import Note

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
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
