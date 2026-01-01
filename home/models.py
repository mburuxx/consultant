from django.db import models


class ContactSubmission(models.Model):
    SUBJECT_CHOICES = [
        ('project', 'Project Inquiry'),
        ('general', 'General'),
        ('audit', 'Audit'),
    ]

    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=20, choices=SUBJECT_CHOICES)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.subject}"


class Testimonial(models.Model):
    client_name = models.CharField(max_length=100)
    company_name = models.CharField(max_length=150, blank=True)
    quote = models.TextField()
    client_logo = models.ImageField(upload_to='testimonials/', blank=True, null=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.client_name