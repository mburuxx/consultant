from django.db import models

class Testimonial(models.Model):
    name = models.CharField(max_length=120)
    company = models.CharField(max_length=120, blank=True)
    role = models.CharField(max_length=120, blank=True)

    quote = models.TextField()
    rating = models.PositiveSmallIntegerField(default=5)

    is_featured = models.BooleanField(default=False)
    is_published = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-is_featured", "-created_at"]

    def __str__(self):
        return f"{self.name} — {self.company}".strip(" —")