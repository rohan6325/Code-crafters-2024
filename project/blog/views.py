from django.shortcuts import render , get_object_or_404
from django.views.generic import ListView , DetailView , CreateView, UpdateView , DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin , UserPassesTestMixin
from .models import post
from django.contrib.auth.models import User
from django.core.paginator import Paginator


class PostListView(ListView):
    model = post
    template_name ='home.html'
    context_object_name ='posts'
    ordering = ['-date']
    paginate_by = 4 
    
class UserPostListView(ListView):
    model = post
    template_name ='User_posts.html'
    context_object_name ='posts'
    paginate_by = 4
    def get_queryset(self):
        user = get_object_or_404(User , username = self.kwargs.get('username'))
        return  post.objects.filter(author=user).order_by('-date')
         
    
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
class PostUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model = post
    login_url='login'
    fields= ['title','content']
    template_name ='update.html'
    def test_func(self):
        post= self.get_object()
        if self.request.user == post.author:
            return True
        return False
class PostDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model = post
    login_url ='login'
    success_url ='/'
    template_name ='post_delete.html'
    def test_func(self):
        post= self.get_object()
        if self.request.user == post.author:
            return True
        return False
    

def about (request):
    API_KEY = open("API_KEY").read()
    current_weather_url="https://weatherapi-com.p.rapidapi.com/current.json"
    
    return render(request, 'index.html')
