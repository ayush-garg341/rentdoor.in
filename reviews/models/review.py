from django.db import models
from django.contrib.auth.models import User


class Reviews(models.Model):
    user_id = models.ForeignKey(User, db_column="user_id", on_delete=models.CASCADE)
    rating = models.IntegerField(blank=True, null=True, default=0)
    title = models.CharField(max_length=500)
    description = models.TextField()
    house_num = models.CharField(max_length=20, blank=True, null=True)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    pin_code = models.CharField(max_length=20)
    country = models.CharField(max_length=50)
    address_line_1 = models.CharField(max_length=255)
    address_line_2 = models.CharField(max_length=255)
    is_active = models.SmallIntegerField(null=True, default=1)
    is_deleted = models.SmallIntegerField(null=True, default=0)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        managed = False
        db_table = "reviews"

    def __str__(self):
        return str(self.title)
