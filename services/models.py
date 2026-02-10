from django.db import models
from django.utils.text import slugify

class Service(models.Model):
    title = models.CharField(max_length=120, unique=True)
    slug = models.SlugField(max_length=140, unique=True, blank=True)

    short_pitch = models.CharField(max_length=200, blank=True)
    benefits = models.TextField(blank=True, help_text="Short paragraph: why this matters.")
    whats_included = models.TextField(blank=True, help_text="Bullet-style text is okay.")
    starting_price = models.DecimalField(max_digits=12, decimal_places=2, null=True, blank=True)

    cta_label = models.CharField(max_length=60, default="Request a Quote")
    is_featured = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    sort_order = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["sort_order", "title"]

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            base = slugify(self.title)
            slug = base
            i = 1
            while Service.objects.filter(slug=slug).exclude(pk=self.pk).exists():
                i += 1
                slug = f"{base}-{i}"
            self.slug = slug
        super().save(*args, **kwargs)