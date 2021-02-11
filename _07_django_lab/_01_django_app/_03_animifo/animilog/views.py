from django.shortcuts import render, HttpResponse
from .models import Post

# Create your views here.
def blogHome(request):
    allPosts = Post.objects.all()
    context = {'allPosts': allPosts}
    return render(request, 'animilog/blogHome.html', context)

def blogPost(request, slug):
    post = Post.objects.filter(slug=slug).first()
    # print(post)
    context = {'post': post}
    return render(request, 'animilog/blogPost.html', context)
