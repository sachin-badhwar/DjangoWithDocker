from django.shortcuts import render
from django.core.mail import send_mail

# Create your views here.
def index(request):
    send_mail('Hello from Sachin Badhwar',
    'Hello there this is a automated mail',
    'sachinbadhwar121@gmail.com',
    ['gelmuyolta@enayu.com','budhwar58@gmail.com'],
    fail_silently=True)
    return render(request, 'send/index.html')
    
