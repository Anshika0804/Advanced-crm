from django.db import models
from users.models import CustomUser

# Create your models here.
class Team(models.Model):
    name = models.CharField(max_length=100)
    created_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="created_teams")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name