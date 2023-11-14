from django.urls import path
from .views import SignUpView, SignInView, AuthRoot

urlpatterns = [
    path('', AuthRoot.as_view()),
    path('login', SignInView.as_view(), name="api-login"),
    path('signup', SignUpView.as_view(), name="api-signup"),
]
