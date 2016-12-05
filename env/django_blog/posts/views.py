from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.core import serializers

from .models import Post
from .forms import PostForm

# CREATE A POST
class PostCreate(CreateView):
    model = Post
    fields = ['title', 'image', "content"]
    template_name = "posts/create.html"
    success_url = "/posts"

# SHOW A POST
class PostDetail(DetailView):
    model = Post
    template_name='posts/detail.html'

# SHOW ALL POSTS
class PostList(ListView):
    model = Post
    context_object_name = 'posts'
    template_name='posts/list.html'

# UPDATE A POST
class PostUpdate(UpdateView):
    model = Post
    fields = ['title', 'image', "content"]
    template_name = "posts/create.html"
    success_url = "/posts"

# DELETE A POST
# class PostDelete(DeleteView):
#     model = Post
#     template_name = "posts/delete.html"
#     success_url = "/posts"

# Ajax endpoint for all Posts
def json_list(request):
    posts = Post.objects.all()
    data = serializers.serialize('json', posts)
    return HttpResponse(data, content_type="application/json")

def post_delete(request, pk=None):
    instance = get_object_or_404(Post, pk=pk)
    instance.delete()
    messages.success(request, "Successfully Deleted.")
    return redirect("posts:list")

# def post_update(request, id=None):
#     instance = get_object_or_404(Post, id=id)
#     form = PostForm(request.POST or None, request.FILES or None, instance=instance)
#     if form.is_valid():
#         instance = form.save(commit=False)
#         instance.save()
#         messages.success(request, "Edit successfully saved!")
#         return redirect("posts:list")
        
#     context = {
#         "title": instance.title,
#         "instance": instance,
#         "form": form,
#         "edit": True,
#     }
#     return render(request, 'posts/create.html', context)

# def post_list(request):
#     queryset = Post.objects.all()
#     context = {
#         "title": 'All Posts',
#         "posts": queryset[::-1] # Reverse the order
#     }
#     return render(request, 'posts/list.html', context)

# def post_detail(request, id=None):
#     instance = get_object_or_404(Post, id=id)
#     context = {
#         "title": "Edit " + instance.title,
#         "instance": instance
#     }
#     return render(request, 'posts/detail.html', context)

# def post_create(request):
#     form = PostForm(request.POST or None, request.FILES or None) 
#     if form.is_valid():
#         instance = form.save(commit=False)
#         # print(form.cleaned_data.get('title'))
#         instance.save()

#         messages.success(request, "Create Post Successful! ")
#         return redirect("posts:list")
#     else:
#         messages.error(request, 'Error. Post not created.')

#     context = {
#         "title": 'Create a New Post',
#         "form": form,
#     }
#     return render(request, "posts/create.html", context)