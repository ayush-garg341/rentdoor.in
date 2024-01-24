from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from django.shortcuts import render, redirect
from reviews.forms.review import CreateReviewForm
import logging

logger = logging.getLogger(__name__)


class Reviews:
    def home_view(request):
        logger.info("Getting reviews list")
        return render(request, "reviews/home.html", {"reviews": []})

    def create_review(request):
        form = CreateReviewForm()
        if request.user and request.user.is_authenticated:
            return render(request, "reviews/create_review.html", {"form": form})
        return redirect("users:login_user")


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
