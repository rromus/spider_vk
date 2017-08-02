from django.conf.urls import url
from . import views
#from login.views import *

urlpatterns = [
#    url(r'^$', views.post_list, name='post_list'),
    url(r'^$', views.filter_list, name='filter_list'),
    url(r'^filter/(?P<filter_id>[0-9]+)/$', views.filter_user, name='filter_user'),

    url(r'^settings/$', views.settings, name='settings'),
    url(r'^logout/$', views.logout_page, name='logout'),
    url(r'^login/$',  views.login_user, name='login'),
#    url(r'^accounts/login/$', 'django.contrib.auth.views.login'), # If user is not login it will redirect to login page
]


