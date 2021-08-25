import follow
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Follow
# Create your views here.

@login_required
def myfollowing(request):
    current_user = request.user
    follow_info = Follow.objects.filter(fan=current_user).order_by('-created')
    follow_name_list = [x.followed.username for x in follow_info]

    context = {
        'following_number': len(follow_name_list),
        'follow_name_list': follow_name_list
    }
    return render(request, 'follow/myfollowing.html', context)
