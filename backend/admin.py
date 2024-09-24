from django.contrib.admin import AdminSite
from django.contrib import admin

class StackWisRAdmin(AdminSite):
  site_header = 'Stackwisr Admin'
  site_title = 'Admin Portal'
  index_title = 'Welcome to the Admin Area'

admin_site = StackWisRAdmin(name='StackwisRAdmin')

admin_site.register(StackWisRAdmin)