from rest_framework.views import APIView
from rest_framework.pagination import PageNumberPagination
from django.shortcuts import get_object_or_404
from blog.models import Blog
from django.core.mail import send_mail
from django.conf import settings
from contact.models import  Contact
from testimonial.models import Testimonial
from careerpath.models import CareerPath
from resources.models import  Resources
from api.serializers import BlogSerializer, CareerPathSerializer, ContactSerializer, TestimonialSerializer, LeadSerializer, ResourcesSerializer
from rest_framework.response import Response
from rest_framework import status

class ContactAPIView(APIView):
  def get(self, request):
    contact = Contact.objects.get(id=1)
    serializer = ContactSerializer(contact)
    return Response(serializer.data)

class BlogPagination(PageNumberPagination):
    page_size = 5  # Number of posts per page
    page_size_query_param = 'page_size'
    max_page_size = 100

class BlogAPIView(APIView):
  
  pagination_class = BlogPagination
  
  def get(self, request, slug=None):
    if slug:
      blogDetail = get_object_or_404(Blog, slug=slug)
      serializer = BlogSerializer(blogDetail)
      return Response(serializer.data)
    else: 
      posts = Blog.objects.all()
      paginator = self.pagination_class()
      paginated_posts  = paginator.paginate_queryset(posts, request)
      
      serializer = BlogSerializer(paginated_posts, many=True)
      return paginator.get_paginated_response(serializer.data)
  

class LatestBlogPostsAPIView(APIView):
  def get(self, request):
    queryset = Blog.objects.all()[:3]  # Limit to the last 3 posts
    serializer = BlogSerializer(queryset, many=True)
    return Response(serializer.data)


class TestimonialAPIView(APIView):
  
  def get(self, request):
    queryset = Testimonial.objects.all()
    serializer = TestimonialSerializer(queryset, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

class CareerPathAPIView(APIView):

  def get(self, request, slug=None):
    if slug:
      try:
        career = CareerPath.objects.get(slug=slug)
        serializer = CareerPathSerializer(career)
      except CareerPath.DoesNotExist:
        return Response({"error": "Career path not found."}, status=status.HTTP_404_NOT_FOUND)
    else:
      careers = CareerPath.objects.all()
      serializer = CareerPathSerializer(careers, many=True)
    
    return Response(serializer.data)
  
class LeadAPIView(APIView):

  def post(self,  request):
    serializer = LeadSerializer(data=request.data)
    if serializer.is_valid():
      serializer.save()
      # lead = request.data
      
      # send_mail(
      #   subject="New Lead Created",
      # message = f"Name: {lead.firstName}\n Email: {lead.email}\n Country: {lead.country}\n Phone: {lead.phone}\n CareerPath: {lead.careerPathName} \n Selected Plan: {lead.selectedPlan}\n Job title: {lead.job-title}\n Company: {lead.company}\n Message: {lead.message} Source: {lead.source}", 
      # from_email=settings.DEFAULT_FROM_EMAIL, 
      # recipient_list=[settings.NOTIFICATION_EMAIL], 
      # fail_silently=False,
      # )
      return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  

class ResourcesPagination(PageNumberPagination):
    page_size = 5  # Number of posts per page
    page_size_query_param = 'page_size'
    max_page_size = 100

class ResourcesAPIView(APIView):

  pagination_class = ResourcesPagination
  
  def get(self, request, slug=None):
    if slug:
      resource = get_object_or_404(Resources, slug=slug)
      serializer = ResourcesSerializer(resource)
    else:
      paginator = self.pagination_class()
      resources = Resources.objects.all()
      paginated_resources = paginator.paginate_queryset(resources, request)
      serializer = ResourcesSerializer(paginated_resources, many=True)
    return  paginator.get_paginated_response(serializer.data)