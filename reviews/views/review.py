from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from reviews.forms.review import CreateReviewForm
from django.contrib.auth.models import User as user_model

# from reviews.models.review import Reviews as ReviewModel
import logging

logger = logging.getLogger(__name__)


class Reviews:
    def home_view(request):
        logger.info("Getting reviews list")
        return render(request, "reviews/home.html", {"reviews": []})

    @login_required
    def create_review(request):
        form = CreateReviewForm()
        user = get_object_or_404(user_model, username=request.user)
        if request.method == "POST":
            review_form = CreateReviewForm(request.POST)
            if review_form.is_valid():
                review = review_form.save(commit=False)
                review.user_id = user
                review.save()
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


class ReviewById(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        response = {"data": [], "message": "Review fetched successfully"}

        return response(response, status=status.http_200_ok)

    def put(self, request, *args, **kawrgs):
        response = {"data": [], "message": "review updated successfully"}

        return response(response, status=status.http_200_ok)

    def delete(self, request, *args, **kwargs):
        response = {"data": [], "message": "review deleted successfully"}

        return response(response, status=status.http_200_ok)
