from django.contrib import admin
from django.urls import path
from .views import  LoginView, RegistrationView, AllJoinUsersView, ValidationOfEmailView, FindUserByTokenView

urlpatterns = [
    path("login/", LoginView.as_view(), name="login"),
    path("registration/", RegistrationView.as_view(), name="registration"),
    path("users/", AllJoinUsersView.as_view(), name ="users"),
    path("check-email/", ValidationOfEmailView.as_view(), name ="check-email"),
    path("find-by-token/", FindUserByTokenView.as_view(), name ="find-by-token")
]