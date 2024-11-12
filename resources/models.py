from django.db import models
from django.utils.text import slugify

class Resources(models.Model):
  title = models.CharField(max_length=150, unique=True)
  slug = models.SlugField(unique=True, blank=True,  null=True)
  description = models.CharField(max_length=500)
  created =  models.DateField(auto_now_add=True)
  

  class Meta:
    ordering = ['-created']

  def save(self, *args, **kwargs):
    if not self.slug:
      self.slug = slugify(self.title)

    super(Resources, self).save(*args, **kwargs)

  def __str__(self):
    return self.title
  
class ResourceFile(models.Model):
  resource = models.ForeignKey(Resources, on_delete=models.CASCADE, related_name='files')
  file = models.FileField(upload_to='resources/')

  def __str__(self):
    return f"File(s) for {self.resource.title}"