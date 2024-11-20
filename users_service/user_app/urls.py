from . import views
from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

urlpatterns = [
    path('', views.root, name="root"),
    path('signin', views.login_user, name="login"),
    path('register', views.register, name="register"),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),  
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),     
    path('test_token/', views.test_token, name='test_token'),     
    path('api/users/<int:user_id>/', views.get_user_details, name='get_user_details'),
]
