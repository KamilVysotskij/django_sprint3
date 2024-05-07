from django.http import Http404
from django.shortcuts import render
from django.shortcuts import get_object_or_404


import datetime


from blog.models import Post, Category


def index(request):
    template = 'blog/index.html'
    post_list = Post.objects.filter(
        pub_date__lte=datetime.datetime.now(),
        is_published=True,
        category__is_published=True,
    ).order_by('-created_at')[:5]
    context = {'post_list': post_list}
    return render(request, template, context)


def post_detail(request, pk):
    template = 'blog/detail.html'
    post = get_object_or_404(
        Post,
        pk=pk,
        is_published=True,
        pub_date__lte=datetime.datetime.now())
    if not post.category.is_published:
        raise Http404
    context = {
        'post': post
    }
    return render(request, template, context)


def category_posts(request, category_slug):
    template = 'blog/category.html'
    category = get_object_or_404(
        Category,
        slug=category_slug,
        is_published=True)
    post_list = Post.objects.filter(
        category=category,
        pub_date__lte=datetime.datetime.now(),
        is_published=True,
    ).order_by('-pub_date')
    context = {
        'category': category,
        'post_list': post_list
    }
    return render(request, template, context)
