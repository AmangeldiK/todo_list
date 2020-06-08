from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.shortcuts import render ,get_object_or_404, redirect
from django.http import HttpResponseRedirect
from django.http import HttpResponseNotFound
from django.utils import timezone
from .models import Post
from .forms import PostForm


def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'todo/post_list.html', {'posts': posts})


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'todo/post_detail.html', {'post': post})


def post_new(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    form = PostForm()
    return render(request, 'todo/post_edit.html', {'form': form})



def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'todo/post_edit.html', {'form': form})


def delete(request, id):
    try:
        post = Post.objects.get(id=id)
        post.delete()
        return HttpResponseRedirect("/")
    except Post.DoesNotExist:
        return HttpResponseNotFound("<h2>Post not found</h2>")
