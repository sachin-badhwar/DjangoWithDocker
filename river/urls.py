from django.urls import path
from . import views

urlpatterns = [
    path('', views.index,name='home'),
    path('roombooking/', views.bookRoom,name='booking'),
    path('rooms/', views.familyroom,name='rooms'),
]