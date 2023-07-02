from django.shortcuts import render, get_object_or_404
from .models import BlogPost

# Create your views here.
def home(request):
    posts = BlogPost.objects.all().order_by('-data') #prosba do bazy o wszystystkie posty
    return render(request, 'home.html', {'posts': posts})

def detail(request, postId):
    # post = BlogPost.objects.get(id=2)
    post = get_object_or_404(BlogPost, id=postId)
    return render(request, 'detail.html', {'post': post})