from django.shortcuts import render, get_object_or_404
from .models import BlogPost

def all_blogs(request):
    blog_posts = BlogPost.objects.order_by('-date')
    return render(request, 'blog/all_blogs.html',{'blog_posts': blog_posts})

def detail(request, blog_id):
    blog = get_object_or_404(BlogPost, pk=blog_id)
    return render(request, 'blog/detail.html',{'blog':blog})