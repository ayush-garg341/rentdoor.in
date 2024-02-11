from django.db import models
from django.contrib.auth.models import User


class ReviewQuerySet(models.QuerySet):
    def locality_search(self, locality, pin_code):
        if pin_code:
            raw_sql = "SELECT r.*, au.first_name from reviews r INNER JOIN auth_user au ON r.user_id = au.id where\
                        MATCH(locality) AGAINST ( %s  in boolean mode ) and r.pin_code = %s order by r.created_at desc"
            reviews = self.raw(raw_sql, [locality, pin_code])
        else:
            raw_sql = "SELECT r.*, au.first_name from reviews r INNER JOIN auth_user au ON r.user_id = au.id\
                        where MATCH(locality) AGAINST ( %s  in boolean mode ) order by r.created_at desc"
            reviews = self.raw(raw_sql, [locality])
        reviews = reviews.prefetch_related("supporting_docs")

        return reviews


class Reviews(models.Model):
    user_id = models.ForeignKey(User, db_column="user_id", on_delete=models.CASCADE)
    rating = models.IntegerField(blank=True, null=True, default=0)
    title = models.CharField(max_length=500)
    description = models.TextField()
    locality = models.TextField()
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    pin_code = models.CharField(max_length=20)
    country = models.CharField(max_length=50, default="India")
    address_line_1 = models.CharField(max_length=255)
    address_line_2 = models.CharField(max_length=255)
    is_active = models.SmallIntegerField(null=True, default=1)
    is_deleted = models.SmallIntegerField(null=True, default=0)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    objects = ReviewQuerySet.as_manager()

    class Meta:
        managed = False
        db_table = "reviews"

    def __str__(self):
        return str(self.title)
