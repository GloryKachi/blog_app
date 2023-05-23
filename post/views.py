from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.urls import reverse_lazy

from .models import Post
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView

from django.views.generic.edit import DeleteView, UpdateView


# Create your views here.

def hello(request):
    posts = Post.objects.all()
    return render(request, 'post/hello.html', {'posts': posts})


class PostListView(ListView):
    model = Post
    template_name = 'post/post_list.html'
    context_object_name = 'posts'


def greet(request):
    return HttpResponse("Hello Cohort 13")


def eat_pizza(request):
    return HttpResponse("I am eating pizza")


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'post/post_detail.html', {'post': post})


class PostDetailView(DetailView):
    model = Post
    template_name = 'post/post_detail.html'
    context_object_name = 'post'


class PostCreateView(CreateView):
    model = Post
    template_name = 'post/post_new.html'
    fields = ['title', 'body', 'author']
    success_url = reverse_lazy("home")


class PostDeleteView(DeleteView):
    model = Post
    template_name = 'post/post_delete.html'
    success_url = reverse_lazy("home")


class PostUpdateView(UpdateView):
    model = Post
    template_name = "post/post_edit.html"
    fields = ['title', 'body']
    success_url = reverse_lazy("home")



