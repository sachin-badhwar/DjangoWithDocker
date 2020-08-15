from django.urls import path
from . import views
from django.conf.urls import url

urlpatterns = [
    path('post/new/',views.PostCreate.as_view() ,name='post_new'),
    path('post/<int:pk>',views.PostDetail.as_view() ,name='post_detail'),
    path('',views.Home.as_view() ,name='homes'),
    
]

#url(r'^post/(?P<pk>[\d]+)/$',views.PostDetail.as_view(),name = 'post_detail'),