from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages

from .models import Post
from .forms import PostForm

# CREATE A POST
def post_create(request):
    form = PostForm(request.POST or None, request.FILES or None) 
    if form.is_valid():
        instance = form.save(commit=False)
        # print(form.cleaned_data.get('title'))
        instance.save()

        messages.success(request, "Create Post Successful! ")
        return redirect("posts:list")
    else:
        messages.error(request, 'Error. Post not created.')

    context = {
        "title": 'Create a New Post',
        "form": form,
    }
    return render(request, "posts/create.html", context)

# SHOW A POST
def post_detail(request, id=None):
    instance = get_object_or_404(Post, id=id)
    context = {
        "title": "Edit " + instance.title,
        "instance": instance
    }
    return render(request, 'posts/detail.html', context)

# SHOW ALL POSTS
def post_list(request):
    queryset = Post.objects.all()
    context = {
        "title": 'All Posts',
        "posts": queryset[::-1] # Reverse the order
    }
    return render(request, 'posts/list.html', context)

# UPDATE A POST
def post_update(request, id=None):
    instance = get_object_or_404(Post, id=id)
    form = PostForm(request.POST or None, request.FILES or None, instance=instance)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        messages.success(request, "Edit successfully saved!")
        return HttpResponseRedirect(instance.get_absolute_url())
        
    context = {
        "title": instance.title,
        "instance": instance,
        "form": form,
        "edit": True,
    }
    return render(request, 'posts/create.html', context)

# DELETE A POST
def post_delete(request, id=None):
    instance = get_object_or_404(Post, id=id)
    instance.delete()
    messages.success(request, "Successfully Deleted.")
    return redirect("posts:list")