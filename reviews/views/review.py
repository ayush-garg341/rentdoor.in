from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.core.files.storage import FileSystemStorage
from django.db import transaction
from django.contrib import messages
from django.db.models import F, Q
from django.http import HttpResponse
from django.contrib.auth.models import User as user_model
from django.conf import settings
from app_users.models.profile import Profile
from libs.helper import create_locality, validate_file_size
from reviews.forms.review import CreateReviewForm, SearchReviewForm
from reviews.models.review import Reviews as ReviewModel
from reviews.models.supporting_docs import SupportingDocs
import logging

logger = logging.getLogger(__name__)


class Reviews:
    def home_view(request):
        profile_pic = ""
        page_number = request.GET.get("page")
        if request.user.is_authenticated:
            profile = Profile.objects.get(user_id=request.user.id)
            profile_pic = profile.profile_pic_link

        reviews = (
            ReviewModel.objects.filter(is_active=True)
            .select_related("user_id")
            .prefetch_related("supporting_docs")
            .annotate(first_name=F("user_id__first_name"))
            .order_by("-created_at")
        )
        paginator = Paginator(reviews, 5)
        reviews = paginator.get_page(page_number)

        return render(
            request,
            "reviews/home.html",
            {"reviews": reviews, "user_profile_link": profile_pic},
        )

    def detail(request, id):
        profile_pic = ""
        if request.user.is_authenticated:
            profile = Profile.objects.get(user_id=request.user.id)
            profile_pic = profile.profile_pic_link

        review = (
            ReviewModel.objects.filter(id=id)
            .select_related("user_id")
            .prefetch_related("supporting_docs")
            .annotate(first_name=F("user_id__first_name"))
            .order_by("-created_at")
        )
        return render(
            request,
            "reviews/review_detail.html",
            {"review": review[0], "user_profile_link": profile_pic},
        )

    @login_required
    def create_review(request):
        form = CreateReviewForm()
        user = get_object_or_404(user_model, username=request.user)
        profile_pic = user.profile.profile_pic_link
        if request.method == "POST":
            review_form = CreateReviewForm(request.POST)
            file_size_valid, file_size_error = validate_file_size(
                request.FILES.getlist("supporting_docs")
            )
            if review_form.is_valid() and file_size_valid:
                with transaction.atomic():
                    review = review_form.save(commit=False)
                    review.locality = create_locality(request.POST)
                    review.user_id = user
                    review.save()
                    if request.FILES:
                        files = request.FILES.getlist("supporting_docs")
                        fs = FileSystemStorage()
                        for request_file in files:
                            doc = SupportingDocs()
                            doc.review = review
                            filename = request_file.name.strip().replace(" ", "_")
                            if filename[-4:] == ".pdf":
                                doc.doc_type = "pdf"
                            else:
                                doc.doc_type = "image"
                            doc.name = filename
                            if request_file:
                                file = fs.save(filename, request_file.file)
                                fileurl = fs.url(file)
                                doc.doc_link = "{}{}".format(
                                    settings.MEDIA_FILE_PREFIX, fileurl
                                )
                            doc.save()
                messages.info(request, "Reviewed added successfully")
                return redirect("reviews:get_all_reviews")
            else:
                if not file_size_valid:
                    messages.info(request, file_size_error)
                return render(
                    request,
                    "reviews/create_review.html",
                    {"form": review_form, "user_profile_link": profile_pic},
                )
        else:
            return render(
                request,
                "reviews/create_review.html",
                {"form": form, "user_profile_link": profile_pic},
            )

    def search_review(request):
        form = SearchReviewForm()
        profile_pic = ""
        if request.user.is_authenticated:
            profile = Profile.objects.get(user_id=request.user.id)
            profile_pic = profile.profile_pic_link
        if request.method == "POST":
            search_form = SearchReviewForm(request.POST)
            if search_form.is_valid():
                page_number = request.GET.get("page")
                pincode = request.POST.get("pin_code")
                locality = request.POST.get("locality")
                if not pincode and not locality:
                    return HttpResponse("Please enter one of the fields")
                if locality:
                    reviews = ReviewModel.objects.locality_search(locality, pincode)
                elif pincode:
                    reviews = (
                        ReviewModel.objects.filter(Q(pin_code=pincode))
                        .select_related("user_id")
                        .prefetch_related("supporting_docs")
                        .annotate(first_name=F("user_id__first_name"))
                        .order_by("-created_at")
                    )
                paginator = Paginator(reviews, 5)
                reviews = paginator.get_page(page_number)
                return render(
                    request,
                    "reviews/home.html",
                    {"reviews": reviews, "user_profile_link": profile_pic},
                )
            else:
                return render(
                    request,
                    "reviews/search_review.html",
                    {"form": search_form, "user_profile_link": profile_pic},
                )
        else:
            return render(
                request,
                "reviews/search_review.html",
                {"form": form, "user_profile_link": profile_pic},
            )
