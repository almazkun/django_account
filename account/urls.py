from django.contrib.auth import views as auth_views
from django.urls import path

from account.views import SignupView

urlpatterns = [
    path("signin/", auth_views.LoginView.as_view(), name="signin"),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
    path("signup/", SignupView.as_view(), name="signup"),
]
