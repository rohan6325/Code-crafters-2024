from django.shortcuts import render
from django.views.generic import ListView , DetailView , CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin , UserPassesTestMixin
from .models import post

def home (request):
    context ={
        'posts':post.objects.all()
    }
    return render(request, 'home.html',context)
class PostListView(ListView):
    model = post
    template_name ='home.html'
    context_object_name ='posts'
    ordering = ['-date']
class PostDetailView(DetailView):
    model = post
    template_name ='post_detail.html'
class PostCreateView(LoginRequiredMixin,CreateView):
    model = post
    login_url='login'
    fields =['title','content']
    template_name ='post_new.html'
    def form_valid(self , form):
        form.instance.author=self.request.user
        return super().form_valid(form)
class PostUpdateView(LoginRequiredMixin,UpdateView):
    model = post
    login_url='login'
    fields= ['title','content']
    template_name ='update.html'
    
def about (request):
    return render(request, 'index.html')
