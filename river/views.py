from django.shortcuts import render, redirect
from django.urls.base import reverse_lazy
from . import forms
from django.contrib import messages
from django.core.paginator import EmptyPage, Paginator, PageNotAnInteger
from .models import FamilyRooms , DeluxRooms
# Create your views here.
def index(request):
    if request.method=='POST':
        print('enter in POST')
        Checkin = str(request.POST['Check in'])
        Checkout = str(request.POST['Check out'])
        Children = (request.POST['Children'])
        Room = (request.POST['Room'])
        print(' Checkin:  ',Checkin,' Checkout: ',Checkout,' Children: ',Children,' Room: ',Room)
        return redirect('booking')
    else:
        print('enter in GET')
        return render(request,'river/index.html')

def bookRoom(request):
    if request.method=='POST':
        print('enter in POST')
        Checkin = str(request.POST['Check in'])
        Checkout = str(request.POST['Check out'])
        Children = (request.POST['Children'])
        Room = (request.POST['Room'])
        print(' Checkin:  ',Checkin,' Checkout: ',Checkout,' Children: ',Children,' Room: ',Room)
        return redirect('booking')
    else:
        print('enter in GET')    
        return render(request,'river/booking.html')

def familyroom(request):
    images_list = FamilyRooms.objects.all()
    page = request.GET.get('page',1)
    print('paginator_page: ',page)
    paginator = Paginator(images_list,3)
    images = paginator.page(page)
    print('images  ',images)
    return render(request,'river/room.html' , {'images':images})