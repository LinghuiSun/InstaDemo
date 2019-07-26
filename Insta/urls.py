"""InstaDemo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from Insta.views import PostlistView, PostdetailView, PostCreateView, PostDeleteView, PostUpdateView, SignUpView, UserProfile, EditProfile

urlpatterns = [
    path('', PostlistView.as_view(), name='home'),
    path('post/<int:pk>/', PostdetailView.as_view(), name='post'),
    path('post/create/', PostCreateView.as_view(), name='make_post'),
    path('post/delete/<int:pk>/', PostDeleteView.as_view(), name='delete_post'),
    path('post/update/<int:pk>', PostUpdateView.as_view(), name='update_post'),
    path('auth/signup/',SignUpView.as_view(), name='signup'),
    path('user_profile/<int:pk>', UserProfile.as_view(), name='profile'),
    path('edit_profile/<int:pk>', EditProfile.as_view(), name='edit_profile'),
]
