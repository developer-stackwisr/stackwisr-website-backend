from rest_framework.serializers import ModelSerializer
from blog.models import Blog
from careerpath.models import CareerPath
from contact.models import Contact
from testimonial.models  import Testimonial
from lead.models import Lead
from resources.models import Resources
from datetime import date

class ContactSerializer(ModelSerializer):

  class Meta:
    model = Contact
    fields = "__all__"

class BlogSerializer(ModelSerializer):

  class Meta:
    model = Blog
    exclude = ['updated',]

  def to_representation(self, instance):
    representation = super().to_representation(instance)
    representation['created'] = date.fromisoformat(representation['created']).strftime("%d, %B %Y")
    return representation

class TestimonialSerializer(ModelSerializer):

  class Meta:
    model = Testimonial
    fields = '__all__'
    
class CareerPathSerializer(ModelSerializer):

  class Meta:
    model = CareerPath
    fields = '__all__'

  def to_representation(self, instance):
    representation = super().to_representation(instance)
    representation['course_start_date'] = date.fromisoformat(representation['course_start_date']).strftime("%d, %B %Y")
    return representation


class LeadSerializer(ModelSerializer):

  class Meta:
    model = Lead
    exclude = ['created']


class ResourcesSerializer(ModelSerializer):

  class Meta:
    model = Resources
    fields = "__all__"