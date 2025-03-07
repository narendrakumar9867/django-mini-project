from django.contrib import admin
from django.urls import path, include
from .views import authView, home, profile, change_password, custom_logout, ForgetPassword, NewPasswordPage
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", home, name="home"),
    path("signup/", authView, name="authView"),
    path("accounts/", include("django.contrib.auth.urls")),
    
    path("profile/", profile, name="profile"),
    path("change_password/", change_password, name="change_password"),
    path("logout/", custom_logout, name="logout"),
    
    path("ForgetPassword/", ForgetPassword, name="forget_password"),
    path("newpasswordpage/<str:user>/", NewPasswordPage, name="new_password"),
]
