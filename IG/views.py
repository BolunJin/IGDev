#from django.shortcuts import render

# Create your views here.
from annoying.decorators import ajax_request

# TemplateView: demo helloworld; ListView: master/detail interface
from django.views.generic import TemplateView, ListView, DetailView
# CRUD using forms
from django.views.generic.edit import CreateView, UpdateView, DeleteView
# Import the model Post for function post in master/detail part
from IG.models import Post, Like
from django.urls import reverse, reverse_lazy
# Mixin use to verify which view can only be used after user's login
from django.contrib.auth.mixins import LoginRequiredMixin

from IG.forms import CustomUserCreationForm

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
class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    template_name = 'post_create.html'
    # what fields users are expected to provide when create a form
    # in this case 2 potential: title and image in model "Post"
    fields = '__all__'
    login_url = 'login' # if not login, jump to 'login' url

class PostUpdateView(UpdateView):
    model = Post
    template_name = 'post_update.html'
    fields = ['title']

class PostDeleteView(DeleteView):
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy("posts")

class SignUp(CreateView):
    form_class = CustomUserCreationForm
    template_name = 'signup.html'
    success_url = reverse_lazy("login")

@ajax_request
def addLike(request):
    post_pk = request.POST.get('post_pk')
    post = Post.objects.get(pk=post_pk)
    try:
        like = Like(post=post, user=request.user)
        like.save()
        result = 1
    except Exception as e:
        like = Like.objects.get(post=post, user=request.user)
        like.delete()
        result = 0

    return {
        'result': result,
        'post_pk': post_pk
    }

@ajax_request
def addComment(request):
    comment_text = request.POST.get('comment_text')
    post_pk = request.POST.get('post_pk')
    post = Post.objects.get(pk=post_pk)
    commenter_info = {}

    try:
        comment = Comment(comment=comment_text, user=request.user, post=post)
        comment.save()

        username = request.user.username

        commenter_info = {
            'username': username,
            'comment_text': comment_text
        }

        result = 1
    except Exception as e:
        print(e)
        result = 0

    return {
        'result': result,
        'post_pk': post_pk,
        'commenter_info': commenter_info
    }