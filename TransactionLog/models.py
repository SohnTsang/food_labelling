from django.db import models
from LabelManagement.models import LabelTemplate
from UserManagement.models import UserInformation


# Model for Transaction and Usage Logs
class TransactionLog(models.Model):
    # A unique identifier for each log entry
    log_id = models.AutoField(primary_key=True)

    # Link to the user who performed the activity
    user = models.ForeignKey(UserInformation, on_delete=models.CASCADE)

    # Type of activity
    activity_type = models.CharField(max_length=255)

    # Timestamp of the activity
    timestamp = models.DateTimeField(auto_now_add=True)

    # Additional details about the activity
    details = models.TextField()

    # Optional: ID of the label template used
    template_used = models.ForeignKey(LabelTemplate, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"{self.user.user.username} - {self.activity_type}"
