from api_dmss.core import models


class PromotionModel(models.Model):
    id = models.UUIDField(primary_key=True, default=models.uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    description = models.TextField()
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    status = models.CharField(max_length=50)

    # ForeignKey
    email_promotion = models.ForeignKey(
        "persistence.EmailPromotionModel",
        null=True, blank=True,
        on_delete=models.SET_NULL
    )