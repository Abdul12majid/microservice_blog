from . import views
from django.urls import path

urlpatterns = [
    path('', views.root, name="root"),
    path('signin', views.login_user, name="login"),
]
