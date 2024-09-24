from django.db import models

class Testimonial(models.Model):
  name = models.CharField(max_length=150, help_text='Testifier\'s name')
  job_description = models.CharField(max_length=250)
  feedback = models.TextField()
  image= models.ImageField(upload_to='testifier-image')

  def __str__(self):
    return self.feedback

