from django.urls import path
from reviews.views.review import Reviews
from reviews.views.healthcheck import HealthCheck

app_name = "reviews"


urlpatterns = [
    path("ping", HealthCheck.as_view(), name="healthcheck"),
    path("", Reviews.home_view, name="get_all_reviews"),
    path("review/<int:id>", Reviews.detail, name="get_review"),
    path("create-review", Reviews.create_review, name="create_review"),
    path("search-review", Reviews.search_review, name="search_review"),
]
