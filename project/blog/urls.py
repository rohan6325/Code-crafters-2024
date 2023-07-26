from . import views
from django.urls import path
from .views import PostListView , PostDetailView , PostCreateView ,PostUpdateView ,PostDeleteView , UserPostListView 
urlpatterns = [
    path("", PostListView.as_view(), name="home"),
    path("userpost/<str:username>", UserPostListView.as_view(), name="User-posts"),
      path("post/<int:pk>/", PostDetailView.as_view(), name="post-detail"),
      path("posts/new/", PostCreateView.as_view(), name="post-create"),
       path("postupdate/<int:pk>/", PostUpdateView.as_view(), name="post-update"),
    path("about",views.about , name='about'),
    path("post/<int:pk>/delete", PostDeleteView.as_view(), name="post-delete")
]
