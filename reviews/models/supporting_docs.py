from django.db import models
from reviews.models.review import Reviews


class SupportingDocs(models.Model):
    review = models.ForeignKey(Reviews, models.CASCADE, related_name="supporting_docs")
    name = models.CharField(max_length=100, blank=True, null=True)
    doc_data = models.TextField()
    doc_link = models.CharField(max_length=500, blank=True, null=True)

    class Meta:
        managed = False
        db_table = "supporting_docs"
