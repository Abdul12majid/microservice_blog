from . import views
from django.urls import path

urlpatterns = [
    path('', views.root, name="root"),
    path('list_posts/', views.list_posts, name="list_posts"),
    #path('api/users/<int:user_id>/', views.user_detail, name='user_detail'),

]
