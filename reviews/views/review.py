from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.db import transaction
from django.contrib import messages
from django.db.models import F, Q
from django.http import HttpResponse
from django.contrib.auth.models import User as user_model
from libs.helper import create_locality
from reviews.forms.review import CreateReviewForm, SearchReviewForm
from reviews.models.review import Reviews as ReviewModel
from reviews.models.supporting_docs import SupportingDocs
import logging
import base64

logger = logging.getLogger(__name__)


class Reviews:
    def home_view(request):
        encoded_data = ""
        page_number = request.GET.get("page")
        if request.user.is_authenticated:
            user = get_object_or_404(user_model, username=request.user)
            if user.profile.profile_pic:
                encoded_data = user.profile.profile_pic

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
            {"reviews": reviews, "user_profile_link": encoded_data},
        )

    @login_required
    def create_review(request):
        form = CreateReviewForm()
        user = get_object_or_404(user_model, username=request.user)
        if request.method == "POST":
            review_form = CreateReviewForm(request.POST)
            if review_form.is_valid():
                with transaction.atomic():
                    review = review_form.save(commit=False)
                    review.locality = create_locality(request.POST)
                    review.user_id = user
                    review.save()
                    if request.FILES:
                        files = request.FILES.getlist("supporting_docs")
                        for file in files:
                            doc = SupportingDocs()
                            doc.review = review
                            filename = file.name
                            if filename[-4:] == ".pdf":
                                doc.doc_type = "pdf"
                            else:
                                doc.doc_type = "image"
                            doc.name = filename
                            doc.doc_data = base64.b64encode(file.read()).decode("utf-8")
                            doc.save()
            messages.info(request, "Reviewed added successfully")
            return redirect("reviews:get_all_reviews")
        else:
            encoded_data = ""
            if user.profile.profile_pic:
                encoded_data = user.profile.profile_pic
            return render(
                request,
                "reviews/create_review.html",
                {"form": form, "user_profile_link": encoded_data},
            )

    def search_review(request):
        form = SearchReviewForm()
        if request.user.is_authenticated:
            user = get_object_or_404(user_model, username=request.user)
            encoded_data = ""
            if user.profile.profile_pic:
                encoded_data = user.profile.profile_pic
        if request.method == "POST":
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
                {"reviews": reviews, "user_profile_link": encoded_data},
            )
        else:
            return render(
                request,
                "reviews/search_review.html",
                {"form": form, "user_profile_link": encoded_data},
            )
