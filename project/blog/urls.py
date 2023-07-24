from . import views
from django.urls import path
from .views import PostListView , PostDetailView , PostCreateView
urlpatterns = [
    path("", PostListView.as_view(), name="home"),
      path("post/<int:pk>/", PostDetailView.as_view(), name="post-detail"),
      path("posts/new/", PostCreateView.as_view(), name="post-create"),
    path("about",views.about , name='about')
]
