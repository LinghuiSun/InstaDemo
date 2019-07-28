from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView,DeleteView
from .models import Post, InstaUser, Like, UserConnection, Comment
from django.urls import reverse_lazy
from Insta.forms import CustomUserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from annoying.decorators import ajax_request
# Create your views here.
class PostlistView(LoginRequiredMixin, ListView):
    model = Post
    template_name = 'home.html'
    login_url = 'login'
    def get_queryset(self):
        current_user = self.request.user
        following = set()
        following.add(current_user)
        for conn in UserConnection.objects.filter(creator=current_user).select_related('following'):
            following.add(conn.following)
        return Post.objects.filter(author__in = following)


class PostdetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'
    # def get_context_data(self, **kwargs):
    #     data = super().get_context_data(**kwargs)
        
    #     liked = Like.objects.filter(post=self.kwargs.get('pk'), user=self.request.user).first()
    #     if liked:
    #         data['liked'] = 1
    #     else:
    #         data['liked'] = 0
    #     return data

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
class ExploreView(LoginRequiredMixin, ListView):
    model = Post
    template_name = 'explore.html'
    login_url = 'login'
    def get_queryset(self):
        return Post.objects.order_by('-posted_on')[:20]


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
        'post_pk': post_pk,
    }

@ajax_request
def togglefollow(request):
    current_user = InstaUser.objects.get(pk=request.user.pk)
    follow_user_pk = request.POST.get('follow_user_pk')
    follow_user = InstaUser.objects.get(pk=follow_user_pk)

    try:
        if current_user != follow_user:
            if request.POST.get('type') == 'follow':
                connection = UserConnection(creator = current_user, following = follow_user)
                connection.save()
            elif request.POST.get('type') == 'unfollow':
                connection = UserConnection.objects.filter(creator = current_user, following = follow_user)
                connection.delete()
            result = 1
        else: 
            result = 0
    except Exception as e:
        print(e)
        result = 0
    
    return {
        'result': result,
        'type': request.POST.get('type'),
        'follow_user_pk': follow_user_pk
    }
@ajax_request
def addComment(request):
    comment_text = request.POST.get('comment_text')
    post_pk = request.POST.get('post_pk')
    post = Post.objects.get(pk = post_pk) 
    commenter_info = {}
    try: 
        comment = Comment(post=post, user=request.user, comment=comment_text)
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