from follow.models import Follow
from typing import List
from django.shortcuts import redirect, render, get_object_or_404
from django.http import HttpResponse
from .models import Post
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.contrib import messages
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView)

#from users.models import Profile
from follow.models import Follow

# function view


def home(request):

    context = {
        'posts': Post.objects.all().order_by('-date_posted'),
        'title': 'blog-home'
    }
    if request.method == 'POST':
        if not request.user.is_authenticated:
            messages.success(request, f'Please login first!')
            return render(request, 'blog/home.html', context)
        current_user = request.user
        befollowed_user= request.POST.get('befollowed')
        print(befollowed_user)
        print(current_user.username)
        if befollowed_user==current_user.username:
            messages.success(request, f'You can not follow yourself!')
            return render(request, 'blog/home.html', context)
        follow_exits=Follow.objects.filter(followed=User.objects.get(username=befollowed_user),
                             fan=current_user)      
        if not follow_exits:
            Follow.objects.create(followed=User.objects.get(username=befollowed_user),
                             fan=current_user)
            messages.success(request, f'You have successfully followed this guy!')
        else:
            messages.success(request, f'You have already followed this guy before!')
        #return redirect('blog-home')
    return render(request, 'blog/home.html', context)

# class-based view, it is a list-type view


class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html'  # the default is <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    ordering = ['-date_posted']  # setup the order of sql query
    paginate_by = 5  # every page has 5 objects


class UserPostListView(ListView):
    model = Post
    # the default is <app>/<model>_<viewtype>.html
    template_name = 'blog/user_posts.html'
    context_object_name = 'posts'
    paginate_by = 5  # every page has 5 objects

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        # query the User objects by username, and the username is from url.

        return Post.objects.filter(author=user).order_by('-date_posted')
        # return all the posts objects posted by the queried user.


class PostDetailView(DetailView):
    model = Post


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


def about(request):
    return render(request, 'blog/about.html')
