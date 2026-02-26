from django.db import models

# Create your models here.
from django.contrib.auth.models import User

class Doctor(models.Model):
    name = models.CharField(max_length=100)
    specialization = models.CharField(max_length=100)
    years_of_experience = models.PositiveIntegerField()
    hospital_name = models.CharField(max_length=150)
    contact_email = models.EmailField()
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="doctors")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name