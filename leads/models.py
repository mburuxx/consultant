from django.db import models

class Lead(models.Model):
    class Status(models.TextChoices):
        NEW = "NEW", "New"
        CONTACTED = "CONTACTED", "Contacted"
        WON = "WON", "Won"
        LOST = "LOST", "Lost"

    name = models.CharField(max_length=120)
    email = models.EmailField(blank=True)
    phone = models.CharField(max_length=40, blank=True)

    company = models.CharField(max_length=120, blank=True)
    message = models.TextField()

    service_interest = models.CharField(max_length=120, blank=True)
    status = models.CharField(max_length=20, choices=Status.choices, default=Status.NEW)

    source = models.CharField(max_length=80, blank=True, help_text="e.g. website form, whatsapp, referral")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.name} ({self.status})"