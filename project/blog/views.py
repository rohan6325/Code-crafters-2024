from django.shortcuts import render , get_object_or_404
from django.views.generic import ListView , DetailView , CreateView, UpdateView , DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin , UserPassesTestMixin
from .models import post
from django.contrib.auth.models import User
from django.core.paginator import Paginator
from django.views.generic.edit import CreateView
from .models import report
from django.contrib.auth.mixins import UserPassesTestMixin
from django.views.generic.edit import CreateView
from .models import report
from .models import Pickup

class PickupCreateView(CreateView):
    model = Pickup
    fields = ['address', 'street_name', 'city', 'time_slot', 'date_of_pickup', 'status', 'type']
    template_name = 'pickup_create.html'
    
class ReportCreateView(LoginRequiredMixin,CreateView):
    model = report
    fields = ['location', 'type', 'status', 'photo']  # include 'photo' field
    template_name ='post_new.html'
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
class ReportDetailView(DetailView):
    model = report
    template_name ='report_detail.html'
    
class ReportListView(UserPassesTestMixin, ListView):
    model = report
    login_url = '/login/'
    template_name = 'report_list.html'  # specify your own template name/location
    context_object_name = 'reports'
    ordering = ['-date']  # order reports by date
    paginate_by = 5  # change this to your preference

    def test_func(self):
        return self.request.user.is_staff
    
class ReportUpdateView(UserPassesTestMixin, UpdateView):
    model = report
    fields = ['status']  # only the status field can be updated
    template_name = 'reportupdate.html'  # specify your own template name/location

    def test_func(self):
        return self.request.user.is_staff
class PostListView(ListView):
    model = post
    login_url='login'
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
    
    
    return render(request, 'index.html')

def landing (request):
    return render(request, 'landing.html')
