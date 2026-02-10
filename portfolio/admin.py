from django.contrib import admin
from .models import Project, ProjectImage

class ProjectImageInline(admin.TabularInline):
    model = ProjectImage
    extra = 1

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ("title", "category", "client_name", "is_featured", "is_published", "sort_order", "updated_at")
    list_filter = ("category", "is_featured", "is_published")
    search_fields = ("title", "client_name", "industry", "stack")
    prepopulated_fields = {"slug": ("title",)}
    ordering = ("sort_order", "-created_at")
    inlines = [ProjectImageInline]