from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from . import forms
from django.contrib.auth.models import User,auth
from django.contrib import messages
from . import models 
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import FormView, CreateView, DeleteView, UpdateView
from django.views.generic.list import ListView
from django.views.generic.base import View
from django.views.generic.detail import SingleObjectMixin , DetailView
from django.urls import reverse, reverse_lazy
#from .forms import  JobApplicantsForm

# Create your views here.
# Using function based views
'''def login(request):
    print('sachin out')
    if request.method=='POST':
        
        form = forms.logins(request.POST)
        print('sachin IN')
        # Now we are checking whether form is valid or not
        if form.is_valid():
            Username = form.cleaned_data['Username']
            password = form.cleaned_data['password']
            user = auth.authenticate(username=Username,password=password)
            # Here user object object will be having either the authenticated user object
            # or None type object if the passed user is wrong
            if user is not None:
                auth.login(request,user)
                print('login done')
                return redirect('view')
            else:
                messages.info(request,'Incorrect Credentials ')
                return redirect('login')
    else:
        form = forms.logins()
        return render(request,'cookies/login.html',{'form':form})'''


'''class loginview(FormView):
    template_name = 'cookies/login.html'
    form_class = forms.logins
    success_url = 'view'   # this is for re-directing 
'''

'''@login_required(login_url='viewa')
def viewPage(request):
    print("outside post")
    if request.method=='POST':
        form = forms.frontpage(request.POST)
        print("in side post")
        if form.is_valid():
            print("form valid")
            name = form.cleaned_data['name']
            creator = form.cleaned_data['creator']
            #date_created = form.cleaned_data['date_created']
            #print(date_created,' : date_created')
            rows = models.Languages(name=name,creator=creator)#,date_created=date_created
            rows.save()
            return redirect('view')
        else:
            messages.info(request,'Invalid form')
            print('form out of work')
            return redirect('view')
    else:
        form = forms.frontpage()
        languages = list(models.Languages.objects.all().values_list('name',flat=True))
        languages = ' '.join(languages)
        print(type(languages))

        return render(request,'cookies/front.html',{'form':form,'languages':languages})
        '''
class GetData(ListView):
    model = models.Languages
    template_name = 'cookies/front.html'
    #context_object_name = 'post'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['post'] = list(models.Languages.objects.all())#.values_list('name',flat=True))
        context['form'] = forms.frontpage
        return context

class PostData(CreateView):
    model = models.Languages
    fields = ('name','creator')
    template_name = 'cookies/front.html'
    success_url = '/cookies/view/'
    context_object_name = 'form'
    
class GetPost(View):
    def get(self, request, *args, **kwargs):
        view = GetData.as_view()
        messages.info(request,'GetData executed ')
        return view(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        view = PostData.as_view()
        return view(request, *args, **kwargs)   

class PostUpdate(UpdateView):
    model = models.Languages
    fields = ('name','creator')
    template_name = 'cookies/front.html'
    success_url =  reverse_lazy('view')

class PostDelete(DeleteView):
    """
    default template - modelname_confirm_delete.html
    """
    model = models.Languages
    template_name = 'cookies/front.html'
    success_url =  reverse_lazy('view')       


def applicants(request, id):
    applicant = models.JobApplicants.objects.get(id=id)
    return render(request, 'cookies/specificApplicants.html', {'data': applicant})









