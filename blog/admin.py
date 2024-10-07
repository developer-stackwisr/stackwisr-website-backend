from django.contrib import admin
from tinymce.widgets import TinyMCE
from django import forms
from .models import Blog


class BlogAdminForm(forms.ModelForm):
  class Meta:
    model = Blog
    fields = '__all__'
    widgets = {
      'body': TinyMCE(attrs={'cols': 80, 'rows': 30}),
  }

class BlogAdmin(admin.ModelAdmin):
  form = BlogAdminForm

admin.site.register(Blog, BlogAdmin)

