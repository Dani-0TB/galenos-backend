from django.urls import path

from .auth.users.views import ApiRoot, SignUp, SignIn

urlpatterns = [
    path('', ApiRoot.as_view()),
    path('signup', SignUp.as_view()),
    path('login', SignIn.as_view())
]
