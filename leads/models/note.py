from django.db import models
from users.models import CustomUser

class Note(models.Model):
    description = models.TextField()
    created_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    lead = models.ForeignKey("leads.Lead", on_delete=models.CASCADE, null=True, blank=True)
    ticket = models.ForeignKey("leads.Ticket", on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f"Note by {self.created_by.name} on {self.created_at}"


