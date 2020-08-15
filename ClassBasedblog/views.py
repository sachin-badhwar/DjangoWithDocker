from django.shortcuts import render, redirect , get_object_or_404
from django.views.generic import View
from django.views.generic.detail import DetailView, SingleObjectMixin 
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView, FormView
from blog.models import Post, Comment , Category
#from django.views import View
from django.urls import reverse_lazy, reverse
from .forms import CommentForm
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
# Create your views here.

@method_decorator(login_required,name='dispatch')
class Home(ListView):
    """
    ListView returns the lists of objects set by model = modelname
    """
    model = Post
    template_name = 'classblog/home.html'
    context_object_name = 'posts'
    ordering = '-pub_date'
    paginate_by = 4
    # Below method provides you the context name with customized data as per your requirements
    '''def get_object(self):
        object = super(Home,self).get_object()
        print('myObject ListView :',object)
        object.view_count +=1
        #object.save()
        return object'''

    '''def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['posts'] = Post.objects.all()
        print('mycontextName listview :',context)
        return context'''

@method_decorator(login_required, name = 'dispatch')
class Dashboard(View):
    """
    'dispatch' method gets the http methods(get,put,post,patch,delete,trace,head,options)
    """
    def get(self, request, *args, **kwargs):
        view = Home.as_view(
            template_name = 'classblog/admin_page.html',
            paginate_by = 4
        )
        return view(request, *args, **kwargs)

@method_decorator(login_required,name='dispatch')
class PostUpdate(UpdateView):
    """
    default template name for updateview = post_form(modelname_form) 
    """
    model = Post
    fields = ('title','category','content')
    template_name = 'classblog/post_form.html'   
    success_url = '/blog/add/'

@method_decorator(login_required,name='dispatch')
class PostDelete(DeleteView):
    # this class based view look for the templateName modelname_confirm_delete(post_confirm_delete.html)
    model = Post
    template_name = 'classblog/post_confirm_delete.html'   
    success_url = reverse_lazy('dashboard')

'''
@method_decorator(login_required,name='dispatch')
class PostDisplay(DetailView):
    """
    SingleObjectMixin : Detail view extends it.
    DetailView returns just the one object set by model = modelname
    default template name for updateview = post_detail(modelname_detail)
    """
    model = Post
    template_name = 'classblog/post_detail.html'
    # context_object_name = 'post' # DetailView gives context object by default as the modelname
    #queryset = Post.objects.all()
    def get_object(self):
        object = super(PostDisplay,self).get_object()
        print('myObject :',object)
        object.view_count +=1
        #object.save()
        return object
    
    def get_context_data(self, **kwargs):
        context = super(PostDisplay,self).get_context_data(**kwargs)
        context['comments'] = Comment.objects.filter(post=self.get_object())
        context['form'] = CommentForm
        print('mycontextName detailview :',context)
        return context
'''
@method_decorator(login_required,name='dispatch')
class PostDisplay(SingleObjectMixin, View):
    """
    SingleObjectMixin : Detail view extends it.
    DetailView returns just the one object set by model = modelname
    default template name for updateview = post_detail(modelname_detail)
    """
    model = Post
    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        #self.postA = Post.objects.get(pk = self.kwargs['pk'])
        print('Myobject:  ',self.object)
        #self.postA.view_count += 1
        self.object.view_count += 1
        #print('Mypost:  ',self.postA)
        #self.postA.save()
        self.object.save()
        #post = Post.objects.get(title=self.postA)
        post = self.get_context_data(object = self.object)
        return render(request, 'classblog/post_detail.html',post)

    def get_context_data(self, **kwargs):
        context = super(PostDisplay,self).get_context_data(**kwargs)
        context['comments'] = Comment.objects.filter(post=self.get_object())
        context['form'] = CommentForm
        print('mycontextName detailview :',context)
        return context

@method_decorator(login_required,name='dispatch')
class PostComment(FormView):
    form_class = CommentForm
    template_name = 'classblog/post_detail.html'
    
    def form_valid(self, form):
        form.instance.by = self.request.user
        post = Post.objects.get(pk=self.kwargs['pk'])
        print('print post: ',post)
        form.instance.post = post
        form.save()
        return super(PostComment, self).form_valid(form)

    def get_success_url(self):
        return reverse('postDetails', kwargs={'pk':self.kwargs['pk']})    

@method_decorator(login_required,name='dispatch')
class PostDetail(View):
    def get(self, request, *args, **kwargs):
        view = PostDisplay.as_view()
        return view(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        view = PostComment.as_view()
        return view(request, *args, **kwargs)    

@method_decorator(login_required,name='dispatch')
class PostCreate(CreateView):
    """
    default template name for updateview = post_form(modelname_form)
    """
    model = Post 
    fields = ('title','category','author','content')
    template_name = 'classblog/post_form.html'
    success_url = '/blog/add/'  # when i comment this line , how it gets re-directed to some other page.  

@method_decorator(login_required,name='dispatch')
class PostCategory(ListView):
    model = Category
    template_name = 'classblog/post_category.html'

    '''def get_queryset(self):
        self.category = Category.objects.get(pk = self.kwargs['pk']) #get_object_or_404(Category, pk = self.kwargs['pk'])
        print('categoryPrint: ',self.category)
        return self.category#Post.objects.filter(category = self.category)'''

    def get_context_data(self, **kwargs):
        context = super(PostCategory,self).get_context_data(**kwargs)
        self.category = Category.objects.get(pk = self.kwargs['pk'])
        context['category'] = self.category
        context['posts'] = Post.objects.filter(category=self.category)
        print('print myContext ',context)    
        return context