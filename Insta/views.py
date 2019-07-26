from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView,DeleteView
from .models import Post, InstaUser
from django.urls import reverse_lazy
from Insta.forms import CustomUserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
class PostlistView(LoginRequiredMixin, ListView):
    model = Post
    template_name = 'home.html'
    login_url = 'login'

class PostdetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'

class PostCreateView(CreateView):
    model = Post
    template_name = 'make_post.html'
    fields = '__all__'
class PostUpdateView(UpdateView):
    model = Post
    template_name = 'update_post.html'
    fields=['title']

class PostDeleteView(DeleteView):
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('home')

class SignUpView(CreateView):
    form_class= CustomUserCreationForm
    template_name = 'sign_up.html'
    success_url = reverse_lazy('login')
class UserProfile(LoginRequiredMixin,DetailView):
    model = InstaUser
    template_name = 'user_profile.html'
    login_url = 'login'
class EditProfile(LoginRequiredMixin,UpdateView):
    model = InstaUser
    template_name = 'edit_profile.html'
    fields=['profile_pic', 'username']
    login_url = 'login'