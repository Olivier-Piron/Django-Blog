from django.shortcuts import render, redirect

from .models import Post

def frontpage(request):
    if 'q' in request.GET:
        q=request.GET['q']
        posts=Post.objects.filter(title__icontains=q)
    else:
        posts=Post.objects.all()


    return render(request, 'blog/frontpage.html', {'posts': posts})

def post_detail(request, slug):
    post = Post.objects.get(slug=slug)

    return render(request, 'blog/post_detail.html', {'post': post})