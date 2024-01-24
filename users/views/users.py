from django.shortcuts import render
from users.forms.users import LoginUserForm, CreateUserForm
import logging

logger = logging.getLogger(__name__)


class User:
    def login_user(request):
        form = LoginUserForm()
        logger.info("Creating user")
        return render(request, "users/login_user.html", {"form": form})

    def create_user(request):
        form = CreateUserForm()
        logger.info("Creating user")
        return render(request, "users/create_user.html", {"form": form})
