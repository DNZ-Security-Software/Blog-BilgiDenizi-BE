from django.shortcuts import get_object_or_404, redirect, render
from .models import Post
from .forms import PostForm


def post_list(request):
    qs = Post.objects.filter(status='p')
    context = {
        "object_list": qs
    }
    return render(request, "blog_api/post_list.html", context)


def post_create(request):
    # form = PostForm(request.POST or None, request.FILES or None)
    form = PostForm()
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect("blog_api:list")
    context = {
        'form': form
    }
    return render(request, "blog_api/post_create.html", context)


def post_detail(request, slug):
    obj = get_object_or_404(Post, slug=slug) 
    context = {
        "object": obj
    }
    return render(request, "blog_api/post_detail.html", context)


def post_update(request, slug):
    obj = get_object_or_404(Post, slug=slug)
    form = PostForm(request.POST or None, request.FILES or None, instance=obj)
    if form.is_valid():
        form.save()
        return redirect("blog_api:list")

    context = {
        "object": obj,
        "form": form
    }
    return render(request, "blog_api/post_update.html", context)


def post_delete(request, slug):
    obj = get_object_or_404(Post, slug=slug)
    if request.method == "POST":
        obj.delete()
        return redirect("blog_api:list")
    context = {
        "object": obj
    }
    return render(request, "blog_api/post_delete.html", context)
