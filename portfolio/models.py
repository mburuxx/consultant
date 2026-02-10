from django.db import models
from django.utils.text import slugify

class Project(models.Model):
    class Category(models.TextChoices):
        POS = "POS", "POS"
        WEBSITE = "WEBSITE", "Website"
        AUTOMATION = "AUTOMATION", "Automation"
        SUPPORT = "SUPPORT", "Support"

    title = models.CharField(max_length=160, unique=True)
    slug = models.SlugField(max_length=180, unique=True, blank=True)

    category = models.CharField(max_length=20, choices=Category.choices, default=Category.WEBSITE)
    client_name = models.CharField(max_length=120, blank=True)
    industry = models.CharField(max_length=120, blank=True)

    problem = models.TextField()
    solution = models.TextField()
    stack = models.CharField(max_length=220, blank=True, help_text="e.g. Django, Postgres, Docker, Nginx")
    outcome = models.TextField(blank=True, help_text="Metrics, improvements, results.")

    testimonial_snippet = models.CharField(max_length=240, blank=True)

    is_featured = models.BooleanField(default=False)
    is_published = models.BooleanField(default=True)
    sort_order = models.PositiveIntegerField(default=0)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["sort_order", "-created_at"]

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            base = slugify(self.title)
            slug = base
            i = 1
            while Project.objects.filter(slug=slug).exclude(pk=self.pk).exists():
                i += 1
                slug = f"{base}-{i}"
            self.slug = slug
        super().save(*args, **kwargs)


class ProjectImage(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name="images")
    image = models.ImageField(upload_to="portfolio/")
    alt_text = models.CharField(max_length=160, blank=True)
    sort_order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["sort_order", "id"]

    def __str__(self):
        return f"{self.project.title} image #{self.id}"