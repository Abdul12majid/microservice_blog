from . import views
from django.urls import path

urlpatterns = [
    path('comments/', views.comments_list_create, name='comments_list_create'),
    path('comments/<uuid:comment_id>/', views.comment_detail, name='comment_detail'),
    
]
