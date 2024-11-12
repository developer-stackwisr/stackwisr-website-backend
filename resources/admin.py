from django.contrib import admin
from .models import Resources, ResourceFile

class ResourceFileInline(admin.TabularInline):  # You can use `admin.StackedInline` for a different layout
  model = ResourceFile
  extra = 1  # Number of empty file slots shown initially

@admin.register(Resources)
class ResourcesAdmin(admin.ModelAdmin):
  inlines = [ResourceFileInline]