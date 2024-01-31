from django.urls import path
from users.views.users import User

app_name = "users"

urlpatterns = [
    path("signup", User.create_user, name="create_user"),
    path("login", User.login_user, name="login_user"),
    path("logout", User.logout_user, name="logout_user"),
]
