from . import views
from django.urls import path
from .views import PostListView , PostDetailView , PostCreateView ,PostUpdateView ,PostDeleteView , UserPostListView,ReportCreateView,ReportDetailView,ReportListView , ReportUpdateView
from .views import PickupCreateView, PickupListView, DashboardView
urlpatterns = [
    path("", views.landing,name="landing"),
    path("posts", PostListView.as_view(), name="home"),
    path("userpost/<str:username>", UserPostListView.as_view(), name="User-posts"),
    path("post/<int:pk>/", PostDetailView.as_view(), name="post-detail"),
    path("posts/new/", PostCreateView.as_view(), name="post-create"),
    path("postupdate/<int:pk>/", PostUpdateView.as_view(), name="post-update"),
    path("about",views.about , name='about'),
    path("post/<int:pk>/delete", PostDeleteView.as_view(), name="post-delete"),
    path('report/new/', ReportCreateView.as_view(), name='report-create'),
    path('report/<int:pk>/', ReportDetailView.as_view(), name='report-detail'),
    path('reports/', ReportListView.as_view(), name='report-list'),
    path('report/<int:pk>/update/', ReportUpdateView.as_view(), name='report-update'),
    path('pickup/new/', PickupCreateView.as_view(), name='pickup-create'),
    path('pickups/', PickupListView.as_view(), name='pickup-list'),
    path('dashboard/', DashboardView.as_view(), name='dashboard')


    
]
