from django.shortcuts import render
from .models import BlogPost

def all_blogs(request):
    blog_posts = BlogPost.objects.order_by('-date')[:3]
    return render(request, 'blog/all_blogs.html',{'blog_posts': blog_posts})
