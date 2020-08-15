from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from . import models

# Create your views here.
def index(request):
    c = 1+1
    return render(request,'index.html',{'c':c})

'''class MovieModel(View):
    model = models.Movie
    template_name = 'index.html'
    def get(self, request, *args, **kwargs):
        data = model.objects.all()
        return render(request,template_name,{'data':data})

    def post(self, request, *args, **kwargs):
        name = request.post['name']
        types = request.post['types']
        name.save()
        types.save()
        temp='thanks for submiting the data'
        return (request,template_name,{'temp':temp})'''

def gets(request):
    print('hello kab')
    #if request.method == 'GET':
    print('hello sab')
    data = models.Movie.objects.get(name='IronMan')
    data1 = data.name
    d = 2
    return render(request,'index.html',{'data1':data1, 'd':d})

def posts(request, *args, **kwargs):
    name = request.post['name']
    types = request.post['types']
    name.save()
    types.save()
    temp='thanks for submiting the data'
    return (request,'index.html',{'temp':temp})        


    
