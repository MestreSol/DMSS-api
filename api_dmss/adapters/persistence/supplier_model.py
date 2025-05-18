from api_dmss.core import models


class SupplierModel(models.Model):
    id = models.UUIDField(primary_key=True, default=models.uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    description = models.TextField()
    contact_info = models.TextField()
    address = models.TextField()
    rating = models.DecimalField(max_digits=3, decimal_places=2)
    reviews_count = models.IntegerField()
    position = models.IntegerField()
    image_url = models.URLField()
    # ForeignKeys
    region = models.ForeignKey(
        "persistence.RegionModel",
        null=True, blank=True,
        on_delete=models.SET_NULL
    )