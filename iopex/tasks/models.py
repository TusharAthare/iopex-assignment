from django.db import models
from users.models import User

# Create your models here.
TASK_STATUS = [
    ("Pending", "Pending"),
    ("In Progress", "In Progress"),
    ("Completed", "Completed")
]

class Tasks(models.Model):
    """Tasks Created By and For Users
    """
    user = models.ForeignKey(User, null=False, on_delete=models.CASCADE)
    title = models.CharField(max_length=1024,null=False)
    description = models.CharField(max_length=1024, blank=True)
    due_date = models.DateTimeField(blank=True, null=True)
    status = models.CharField(
        choices=TASK_STATUS,
        default="Pending",
        max_length=1024
    )
    created_at = models.DateTimeField(auto_created=True,auto_now=True)
    updated_at = models.DateTimeField(auto_created=True,auto_now=True)
    
    

