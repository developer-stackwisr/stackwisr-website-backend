from django.contrib import admin
from .models import Lead
import csv
from django.http import HttpResponse

def export_As_csv(modeladmin, request, queryset):
  response =  HttpResponse(content_type='text/csv')
  response['Content-Disposition'] = 'attachment; filename="leads_data.csv"'

  writer = csv.writer(response)

  field_names = [field.name for field in modeladmin.model._meta.fields]

  # Write the first row as the header row with the field names
  writer.writerow(field_names)

  # Iterate through the queryset and write each object's field values as columns
  for obj in queryset:
    row = [getattr(obj, field) for field in field_names]
    writer.writerow(row)

  return response

export_As_csv.short_description = "Export selected items as CSV"

class LeadAdmin(admin.ModelAdmin):

  actions  = [export_As_csv]

  def get_readonly_fields(self, request, obj=None):
    return [field.name for field in self.model._meta.fields]


admin.site.register(Lead, LeadAdmin)