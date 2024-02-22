from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.hashers import make_password
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.contrib import messages

from django.contrib.auth.models import User as user_model
from app_users.forms.users import LoginUserForm, CreateUserForm, CreateProfileForm
from libs.helper import validate_file_size
from libs.blob_uploader import DigitalOceanUploader
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
                logger.exception("Exception occurred while login", str(e))
                return redirect("app_users:create_user")
            pwd = request.POST.get("password")
            auth_user = authenticate(request, username=uname, password=pwd)
            if auth_user:
                login(request, auth_user)
                request.session["user"] = uname
                return redirect("reviews:create_review")
            else:
                return render(request, "users/login_user.html", {"form": form})

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
            user_form = CreateUserForm(request.POST)
            profile_form = CreateProfileForm(request.POST)
            file_size_valid, file_size_error = validate_file_size(
                [request.FILES.get("profile_pic")]
            )
            if user_form.is_valid() and profile_form.is_valid() and file_size_valid:
                first_name = request.POST.get("first_name")
                last_name = request.POST.get("last_name")
                username = request.POST.get("username")
                email = request.POST.get("email")
                pwd = make_password(request.POST.get("password"))
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
                    file = request.FILES.get("profile_pic")
                    if file:
                        filename = file.name
                        user.profile.profile_pic_link = (
                            DigitalOceanUploader().upload_file(
                                file, filename, "rent-docs", True
                            )
                        )
                    # user.profile.profile_pic = (
                    # base64.b64encode(
                    # request.FILES.get("profile_pic").read()
                    # ).decode("utf-8")
                    # if request.FILES.get("profile_pic")
                    # else ""
                    # )
                    user.save()
                    messages.info(request, "User created successfully")
                    return redirect("app_users:login_user")
            else:
                if not file_size_valid:
                    messages.info(request, file_size_error)
                return render(
                    request,
                    "users/create_user.html",
                    {"form": user_form, "profile": profile_form},
                )
        return render(
            request, "users/create_user.html", {"form": form, "profile": profile_form}
        )

    @login_required
    def profile(request):
        user_id = request.user.id
        user = user_model.objects.get(id=user_id)
        return render(
            request,
            "users/user_detail.html",
            {"user": user, "user_profile_link": user.profile.profile_pic},
        )
