from django.db import models
from django.utils.text import slugify
from datetime import datetime
class CareerPath(models.Model):
  img_display = models.ImageField(upload_to='career-path-images/', blank=True, null=True)
  career_name = models.CharField(max_length=150)
  slug = models.SlugField(unique=True, max_length=160, blank=True)
  description = models.CharField(max_length=350)
  rating = models.DecimalField(max_digits=3, decimal_places=1, help_text="i.e. 4.5")
  language = models.CharField(max_length=20,)
  enroll_now_link = models.CharField(max_length=150, blank=True, null=True)
  what_you_will_learn_list = models.JSONField(default=list)
  skills_you_will_gain = models.JSONField(default=list)
  potential_jobs = models.JSONField(default=list)
  course_start_date = models.DateField(help_text="Date course starts", default=datetime.now())

  def save(self, *args, **kwargs):
    if not self.slug:
      self.slug = slugify(self.career_name)
    super(CareerPath, self).save(*args, **kwargs)

  def __str__(self) -> str:
    return self.career_name

