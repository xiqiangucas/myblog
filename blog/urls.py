from django.conf.urls import url
from blog.views import index,article_page,edit_page,edit_action

urlpatterns = [
    url(r'^index/$', index),
    url(r'^article/(?P<article_id>[0-9]+)$',article_page,name='article_page'),
    url(r'^edit/(?P<article_id>[0-9]+)$',edit_page,name='edit_page'),
    url(r'^edit/action$',edit_action,name='edit_action'),
]