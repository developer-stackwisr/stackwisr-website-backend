from django.db import models


class Contact(models.Model):
  email = models.JSONField(default=list)
  phone_number = models.JSONField(default=list)

  class Meta:
    verbose_name = "Contact Detail"
    verbose_name_plural = "Contact Details"

  def __str__(self):
    return self.email 

