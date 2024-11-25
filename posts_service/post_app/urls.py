from . import views
from django.urls import path

urlpatterns = [
    path('', views.root, name="root"),
    path('list_posts/', views.list_posts, name="list_posts"),
    #path('api/users/<int:user_id>/', views.user_detail, name='user_detail'),
    path('create_post/', views.create_post, name="create_post"),
    path('post/<uuid:post_id>/', views.retrieve_post, name='retrieve_post'),
    path('posts/<uuid:post_id>/', views.delete_post, name='delete_post'),

]
