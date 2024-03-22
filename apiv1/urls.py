from django.urls import path

from . import views


urlpatterns = [
    path("login", views.login, name="login"),
    path("signup", views.signup, name="signup"),
    path("logout", views.logout, name="logout"),
    path("settings", views.settings, name="settings"),
    path("current_user", views.current_user, name="current_user"),
    path("chat/<slug:id>", views.chat, name="chat"),
    path("", views.index, name="index"),
]
