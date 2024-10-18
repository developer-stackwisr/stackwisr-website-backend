from rest_framework.views import APIView
from rest_framework.pagination import PageNumberPagination
from django.shortcuts import get_object_or_404
from blog.models import Blog
from contact.models import  Contact
from testimonial.models import Testimonial
from careerpath.models import CareerPath
from api.serializers import BlogSerializer, CareerPathSerializer, ContactSerializer, TestimonialSerializer, LeadSerializer
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
      return Response(status=status.HTTP_201_CREATED)
    return Response(status=status.HTTP_400_BAD_REQUEST)