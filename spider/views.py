from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect
from django.conf import settings
#from django.contrib.auth import authenticate, login
from .models import Post
from .models import Settings

# Create your views here.


def post_list(request):
#    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    #if not request.user.is_authenticated():
        #return render(request, 'myapp/login_error.html')
        #return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))
    
    if not request.user.is_authenticated(): 
        #if user.is_active:
        #login(request, user)
        return render(request, 'blog/post_list.html',)
    
    if request.method == "GET":
        id_post = request.GET.get('id')
        action = request.GET.get('action') 
        if(id_post and action=='hide'):
            print("get:",request.GET)
            post_hide = get_object_or_404(Post, pk=id_post)
            
            #post_hide = Post.objects.filter(id=id_post)
            #return render(request, 'blog/post_list.html', {'posts': post_hide})

            post_hide.status = 'hide'
            post_hide.save()



    posts = Post.objects.filter(status='new').order_by('-date')[:100]
    
    return render(request, 'blog/post_list.html', {'posts': posts})


def post_action_hide(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return redirect('post')



def settings(requst):
    settings = Settings.objects.all()
    return render(requst, 'blog/settings.html', {'settings': settings})

def logout_view(request):
    logout(request)
    # Redirect to a success page.

