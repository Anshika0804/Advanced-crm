from django.db import models
from users.models import CustomUser

class Attachment(models.Model):
    file = models.FileField(upload_to='attachments/')
    uploaded_by = models.ForeignKey(CustomUser, null=True, blank=True,  on_delete=models.CASCADE)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    lead = models.ForeignKey("leads.Lead", on_delete=models.CASCADE, null=True, blank=True)
    ticket = models.ForeignKey("leads.Ticket", on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f"Attachment by {self.uploaded_by.name} on {self.uploaded_at}"
