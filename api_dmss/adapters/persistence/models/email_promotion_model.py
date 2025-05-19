from api_dmss.core import models


class EmailPromotionModel(models.Model):
    id = models.UUIDField(primary_key=True, default=models.uuid.uuid4, editable=False)
    subject = models.CharField(max_length=255)
    body = models.TextField()
    send_date = models.DateTimeField()
    status = models.CharField(max_length=50)

    # ForeignKey
    promotion = models.ForeignKey(
        "persistence.PromotionModel",
        null=True, blank=True,
        on_delete=models.SET_NULL
    )