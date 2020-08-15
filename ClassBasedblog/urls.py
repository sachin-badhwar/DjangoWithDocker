from django.urls import path
from . import views
from django.conf.urls import url
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('post/cat/<int:pk>/',views.PostCategory.as_view() ,name='post_by_category'),
    path('logout/',auth_views.LogoutView.as_view() ,name='logout'),
    path('login/',auth_views.LoginView.as_view(template_name='classblog/login.html') ,name='login'),
    path('dashboard/',views.Dashboard.as_view() ,name='dashboard'),
    path('post/<int:pk>/',views.PostDetail.as_view() ,name='postDetails'),
    path('post/<int:pk>/delete/',views.PostDelete.as_view() ,name='post_delete'),
    path('post/<int:pk>/update/',views.PostUpdate.as_view() ,name='post_update'),
    path('add/',views.PostCreate.as_view() ,name='post_add'),
    path('',views.Home.as_view() ,name='homeA'),
    
    
]
#path('post/<int:pk>/update',views.PostUpdate.as_view() ,name='post_update'),