from django.db import models
from users.models import CustomUser
from leads.models import Lead

# Create your models here.
class Notification(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="notifications")
    lead = models.ForeignKey(Lead, on_delete=models.CASCADE, null=True, blank = True)
    message = models.TextField()
    is_read = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.message[:30]}"
    
    