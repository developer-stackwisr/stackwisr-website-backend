from django.db import models

class Lead(models.Model):
  selectedPlan = models.CharField(max_length=150)
  careerPathName = models.CharField(max_length=150) 
  firstName = models.CharField(max_length=150)
  lastName = models.CharField(max_length=150)
  email = models.EmailField(max_length=254)
  phone = models.CharField(max_length=15)
  source = models.CharField(max_length=20, blank=True, null=True)
  jobTitle = models.CharField(max_length=100, blank=True, null=True)
  company = models.CharField(max_length=150, blank=True, null=True)
  message = models.CharField(max_length=500, blank=True, null=True)
  subscribe=models.CharField(max_length=3, null=True, blank=True)
  country=models.TextField()
  created = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return f"Plan: {self.selectedPlan}, Careerpath: {self.careerPathName} from {self.country}"