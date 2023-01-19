from django.shortcuts import render
from django.views.generic import DetailView,ListView,CreateView
from .models import Post,Contact
from .form import MyContact


#def index(request):
    #index_data=Post.objects.all()
    #return render(request, 'myapp/index.html', {'list':index_data})
class index(ListView):
    model = Post
    fields=['title', 'slug', 'created_on','photo']
    template_name= 'myapp/index.html'
    success_url='/about/'
  
class about(DetailView):
    model = Post
    template_name= 'myapp/about.html'
    

#def about(request):
    #return render(request, 'myapp/about.html')

#def blog(request):
    #return render(request, 'myapp/blog.html')
class blog(DetailView):
    model = Post
    #fields=['title', 'slug', 'created_on','photo']
    template_name= 'myapp/blog.html'


#def contact(request):
    #return render(request, 'myapp/contact.html')
class listContect(CreateView):
    form_class = MyContact
    template_name='myapp/contact.html'
    success_url='/contact/'

class features(DetailView):
    model = Post
    #fields=['title', 'slug', 'created_on','photo']
    template_name= 'myapp/features.html'

#def features(request):
    #return render(request, 'myapp/features.html')


