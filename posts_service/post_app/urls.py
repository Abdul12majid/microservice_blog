from . import views
from django.urls import path

urlpatterns = [
    path('', views.root, name="root"),
    path('all_posts/', views.posts, name="posts"),
]
