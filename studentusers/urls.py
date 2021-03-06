from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path("", auth_views.LoginView.as_view(redirect_authenticated_user=True, template_name="studentusers/login.html"), name="login"),
    path("logout", auth_views.LogoutView.as_view(template_name="studentusers/logout.html"), name="logout"),
    path("register/", views.register, name="register"),
    path("students/", views.students, name="students"),
]
