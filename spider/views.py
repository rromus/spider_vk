from django.shortcuts import render_to_response, render, get_object_or_404
from django.shortcuts import redirect
from django.db.models import Q
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.template import RequestContext
from django.contrib.auth import authenticate, login

from .models import Vkpost, Vkuser, Vkcity
from .models import Filter


# Create your views here.


def filter_list(request):
    # print(request.user)
    user_filters = Filter.objects.filter(user=request.user)

    return render(request, 
                'spider/filter_list.html',
                {'filters': user_filters,}
                )

def filter_user(request, filter_id):
    if not request.user.is_authenticated():
        return redirect('/')

    user_filter = get_object_or_404(Filter, id=filter_id)
    if(request.user != user_filter.user):
        return redirect('/')

    
    if request.method == "POST":
        action_id = request.POST.get('id')
        action = request.POST.get('action') 
        print(action_id, action)
        if(action_id and action=='hide_post'):
            # print("post:",request.POST)
            post_hide = get_object_or_404(Vkpost, pk=action_id)
            post_hide.user_ignore_post.add(request.user)
            return redirect('.')

        if(action_id and action=='author_ignor'):
            # print("author_ignor:", action_id)
            # print(author_ignor)
            author_ignor = get_object_or_404(Vkuser, user_id=action_id)
            user_filter.author_ignore.add(author_ignor)
            return redirect('.')


    f_crit = Q() 
    for w in user_filter.mandatory_word.split(","):
        f_crit.add(Q(text__icontains=w.strip()), Q.OR)

    ignore_crit = Q() 
    for w in user_filter.ignore_word.split(","):
        ignore_crit.add(Q(text__icontains=w.strip()), Q.OR)
    
    post_all = Vkpost.objects.exclude(user_ignore_post=request.user)\
        .exclude(author__filter__name=user_filter)\
        .filter(f_crit).exclude(ignore_crit)\
        .order_by('-date')\

    all_count_post = len(post_all)
    posts = post_all[:50]
    
    return render(request, 
                'spider/news_post.html', 
                { 'posts': posts, 
                  'all_count_post':all_count_post,
                  'current_count_post':len(posts),
                  'filter':user_filter,
                }
            )


def post_action_hide(request, pk):
    post = get_object_or_404(Post, pk=pk)
    print("---- post_action_hide")
    return redirect('/')



def settings(requst):
    settings = Settings.objects.all()
    return render(requst, 'spider/settings.html', {'settings': settings})


def login_user(request):
    logout(request)
    username = password = ''
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect('/')
        else:
            return render(request, 'spider/login.html', {'errors': True})

    return render(request, 'spider/login.html')


def logout_page(request):
    logout(request)
    return redirect('/')
    return HttpResponseRedirect('/')
