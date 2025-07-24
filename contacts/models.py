from django.db import models
from django.contrib.auth import get_user_model
from leads.models import Lead  

User = get_user_model()

class Contact(models.Model):
    lead = models.ForeignKey(Lead, on_delete=models.CASCADE, related_name='contacts')
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100, blank=True, null=True)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='contacts')

    def __str__(self):
        return f"{self.first_name} {self.last_name or ''}".strip()
