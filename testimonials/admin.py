from django.contrib import admin
from .models import Testimonial

@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ("name", "company", "rating", "is_featured", "is_published", "created_at")
    list_filter = ("is_featured", "is_published", "rating")
    search_fields = ("name", "company", "quote")