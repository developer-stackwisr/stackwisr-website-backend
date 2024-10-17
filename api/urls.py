from django.urls import path
from .views import BlogAPIView, CareerPathAPIView, LatestBlogPostsAPIView, TestimonialAPIView

urlpatterns = [
  path('blog/posts/', BlogAPIView.as_view()),
  path('blog/post/<str:slug>/', BlogAPIView.as_view()),
  path('blog/latest-posts/', LatestBlogPostsAPIView.as_view()),
  path('testimonies/', TestimonialAPIView.as_view(), name='testimonies'),
  path('careerpaths/', CareerPathAPIView.as_view(), name='careerpath-list'),
  path('careerpaths/<slug:slug>/', CareerPathAPIView.as_view(), name='careerpath-detail'),
]
