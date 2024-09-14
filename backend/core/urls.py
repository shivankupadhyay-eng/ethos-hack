from django.urls import path
from .views import LoginView, SignupView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

urlpatterns=[
    path('signup/',SignupView.as_view(),name="signup"),
    path('login/',LoginView.as_view(),name="login"),
    path('token_refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('get_token/',TokenObtainPairView.as_view(),name='get_token'),
    path('verify_token/',TokenVerifyView.as_view(),name='token_verify')
]