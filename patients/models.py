from django.db import models
from django.contrib.auth.models import User

class Patient(models.Model):
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="patients")
    name = models.CharField(max_length=100)
    age = models.PositiveIntegerField()
    gender = models.CharField(max_length=10, choices=[("Male", "Male"), ("Female", "Female"), ("Other", "Other")])
    symptoms = models.TextField(blank=True)
    diagnosis_status = models.CharField(
        max_length=20,
        choices=[("pending", "Pending"), ("cancerous", "Cancerous"), ("non-cancerous", "Non-cancerous"),('in_review', 'In Review'),],
        default="pending"
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name