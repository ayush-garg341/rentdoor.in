from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.db import transaction
from django.db.models import F
from django.contrib.auth.models import User as user_model
from reviews.forms.review import CreateReviewForm
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
                encoded_data = encoded_data[2 : len(encoded_data) - 1]

        reviews = (
            ReviewModel.objects.filter(is_active=True)
            .select_related("user_id")
            .values(
                "id",
                "title",
                "description",
                "address_line_1",
                "address_line_2",
                "created_at",
                "user_id__first_name",
            )
            .annotate(first_name=F("user_id__first_name"))
            .order_by("-created_at")
        )
        paginator = Paginator(reviews, 10)
        reviews = paginator.get_page(page_number)

        for review in reviews:
            docs = SupportingDocs.objects.filter(review=review["id"])
            review["docs"] = docs

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
                    review.user_id = user
                    review.save()
                    print(request.FILES)
                    if request.FILES:
                        files = request.FILES.getlist("supporting_docs")
                        for file in files:
                            doc = SupportingDocs()
                            doc.review = review
                            doc.name = file.name
                            doc.doc_data = base64.b64decode(file.read())
                            doc.save()
            else:
                logger.error(review_form.errors())
            return redirect("reviews:create_review")
        else:
            encoded_data = ""
            if user.profile.profile_pic:
                encoded_data = user.profile.profile_pic
                encoded_data = encoded_data[2 : len(encoded_data) - 1]
            return render(
                request,
                "reviews/create_review.html",
                {"form": form, "user_profile_link": encoded_data},
            )
