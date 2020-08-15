from django.shortcuts import render, redirect
from django.views import View
from .models import Post
from .forms import PostForm
from django import forms
# Create your views here.
class Home(View):
    def get(self,request):
        posts = Post.objects.all()
        return render(request,'blog/home.html',{'posts':posts})

class PostDetail(View):
    def get(self, request, pk):
        post = Post.objects.get(pk=pk)
        return render(request,'blog/post_detail.html',{'post':post})

class PostCreate(View):
    def get(self, request):
        form = PostForm
        return render(request,'blog/post_form.html',{'form':form})

    def post(self, request):
        form = PostForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data.get('title')
            if 'KRK' in title:
                raise forms.ValidationError("This is not valid name")
            form.save()
            return redirect('homes')
        return render(request,'blog/post_form.html',{'form':form})        
