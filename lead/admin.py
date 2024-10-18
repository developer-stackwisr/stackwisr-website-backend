from django.contrib import admin
from .models import Lead

class LeadAdmin(admin.ModelAdmin):
  def get_readonly_fields(self, request, obj=None):
    return [field.name for field in self.model._meta.fields]


admin.site.register(Lead, LeadAdmin)