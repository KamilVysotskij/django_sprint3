from django.http import Http404
from django.shortcuts import render, get_object_or_404

from blog.models import Post, Category


def index(request):
    template = 'blog/index.html'
    post_list = Post.published_objects.all().filter(
        category__is_published=True)[:5]
    context = {'post_list': post_list}
    return render(request, template, context)


def post_detail(request, pk):
    template = 'blog/detail.html'
    post = get_object_or_404(
        Post.published_objects.all(),
        pk=pk)
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
    post_list = Post.published_objects.all().filter(
        category=category).order_by('-pub_date')
    context = {
        'category': category,
        'post_list': post_list
    }
    return render(request, template, context)
