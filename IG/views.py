#from django.shortcuts import render

# Create your views here.

# TemplateView: demo helloworld; ListView: master/detail interface
from django.views.generic import TemplateView, ListView, DetailView
# CRUD using forms
from django.views.generic.edit import CreateView, UpdateView, DeleteView
# Import the model Post for function post in master/detail part
from IG.models import Post
from django.urls import reverse, reverse_lazy

# define view based on what is to achieve -> add view to url -> write template you want to render

# static page
class HelloWorld(TemplateView):
    # To point out which template to render by this view
    template_name = 'test.html'

# picture post with master/detail structure
# master view
class PostsView(ListView):
    model = Post
    template_name = 'index.html'

# detail view
class PostDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'

# view used to user create form
class PostCreateView(CreateView):
    model = Post
    template_name = 'post_create.html'
    # what fields users are expected to provide when create a form
    # in this case 2 potential: title and image in model "Post"
    fields = '__all__'

class PostUpdateView(UpdateView):
    model = Post
    template_name = 'post_update.html'
    fields = ['title']

class PostDeleteView(DeleteView):
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy("posts")