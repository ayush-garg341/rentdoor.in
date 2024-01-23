from django.urls import path
from reviews.views.review import Reviews, ReviewById
from reviews.views.healthcheck import HealthCheck

urlpatterns = [
    path("ping", HealthCheck.as_view(), name="healthcheck"),
    path("", Reviews.as_view(), name="get_all_reviews"),
    path("review", Reviews.as_view(), name="add_review"),
    path("review/<int:id>", ReviewById.as_view(), name="get_particular_review"),
]
