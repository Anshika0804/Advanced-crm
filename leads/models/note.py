from django.db import models
from .ticket import Ticket
from django.contrib.auth import get_user_model

User = get_user_model()

class Note(models.Model):
    ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE, related_name='notes')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Note by {self.author} on Ticket {self.ticket.id}"
