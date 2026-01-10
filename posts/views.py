from django.shortcuts import render, get_object_or_404
from .models import Post, Category


def home(request):
    posts = Post.objects.all()
    categories = Category.objects.all()
    return render(request, 'home.html', {
        'posts': posts,
        'categories': categories
    })


def post_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    return render(request, 'post_detail.html', {'post': post})


def category_posts(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    posts = Post.objects.filter(category=category)
    return render(request, 'category_posts.html', {
        'category': category,
        'posts': posts
    })
