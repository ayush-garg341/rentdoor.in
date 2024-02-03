from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.hashers import make_password
from django.db import transaction

from django.contrib.auth.models import User as user_model
from app_users.forms.users import LoginUserForm, CreateUserForm, CreateProfileForm
import base64
import logging

logger = logging.getLogger(__name__)


class User:
    def login_user(request):
        form = LoginUserForm()
        if request.method == "POST":
            uname = request.POST.get("username")
            try:
                _ = get_object_or_404(user_model, username=uname)
            except Exception as e:
                logger.exception("Exception occurred", str(e))
                return redirect("app_users:create_user")
            pwd = request.POST.get("password")
            auth_user = authenticate(request, username=uname, password=pwd)
            login(request, auth_user)
            if auth_user:
                request.session["user"] = uname
                return redirect("reviews:create_review")
            else:
                return HttpResponse("Please enter valid Username or Password.")

        return render(request, "users/login_user.html", {"form": form})

    def logout_user(request):
        for sesskey in list(request.session.keys()):
            del request.session[sesskey]
        logout(request)
        return redirect("reviews:get_all_reviews")

    def create_user(request):
        form = CreateUserForm()
        profile_form = CreateProfileForm()
        if request.method == "POST":
            first_name = request.POST.get("first_name")
            last_name = request.POST.get("last_name")
            username = request.POST.get("username")
            email = request.POST.get("email")
            pwd = make_password(request.POST.get("password"))
            if user_model.objects.filter(username=username).count() > 0:
                # pass error to the form object if already exists
                return HttpResponse("Username already exists.")
            else:
                with transaction.atomic():
                    user = user_model(
                        first_name=first_name,
                        last_name=last_name,
                        username=username,
                        email=email,
                        password=pwd,
                    )
                    user.save()
                    user.profile.job_title = request.POST.get("job_title")
                    user.profile.profile_pic = (
                        base64.b64encode(request.FILES.get("profile_pic").read())
                        if request.FILES.get("profile_pic")
                        else ""
                    )
                    user.save()
                    return redirect("app_users:login_user")
        return render(
            request, "users/create_user.html", {"form": form, "profile": profile_form}
        )
