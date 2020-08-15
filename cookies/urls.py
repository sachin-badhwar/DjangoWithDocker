from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    
    path('viewa/',auth_views.LoginView.as_view(template_name='cookies/login.html'), name='viewa'),
    path('logout/',auth_views.LogoutView.as_view(),name='logout'),
    path('view/<int:pk>/update',views.PostUpdate.as_view(),name='UpdateView'),
    path('view/<int:pk>/delete',views.PostDelete.as_view(),name='DeleteView'),
    path('view/',views.GetPost.as_view(),name='view'),
    path('applicants/<int:id>/',views.applicants,name='applicants'),
    #path('viewa',views.login,name='viewa'),
    #path('viewa',views.loginview.as_view(),name='viewa'),
    #path('view/',views.viewPage,name='view'),
    
]

urlpatterns = urlpatterns + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT) 
#path('login',views.login,name='login'), 