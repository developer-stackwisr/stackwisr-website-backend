from django.db import models
from tinymce import models as tinymce_models
from django.utils.text import slugify
from .validators import validate_image
from bs4 import BeautifulSoup

class Blog(models.Model):
  image = models.ImageField(upload_to='blog_images/', blank=True, null=True, validators=[validate_image])
  slug = models.SlugField(unique=True, max_length=160, blank=True)
  author = models.CharField(help_text='Author\'s name', max_length=50)
  title = models.CharField(max_length=250)
  body = tinymce_models.HTMLField()
  created = models.DateField(auto_now_add=True)
  updated = models.DateField(auto_now=True)
  meta_description = models.TextField(blank=True, null=True)

  class Meta:
    ordering = ['-created']
  
  def save(self, *args, **kwargs):
    if not self.slug:
      self.slug = slugify(self.title)

    if not self.meta_description:
      soup = BeautifulSoup(self.body, 'html.parser')
      self.meta_description = soup.get_text()[:350]
    
    super(Blog, self).save(*args, **kwargs)

  def __str__(self) -> str:
    return f"{self.title} by {self.author} on {self.created}"