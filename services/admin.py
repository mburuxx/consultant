from django.contrib import admin
from .models import Service

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ("title", "starting_price", "is_featured", "is_active", "sort_order", "updated_at")
    list_filter = ("is_featured", "is_active")
    search_fields = ("title", "short_pitch")
    prepopulated_fields = {"slug": ("title",)}
    ordering = ("sort_order", "title")