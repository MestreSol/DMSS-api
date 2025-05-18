from api_dmss.core import models


class ProductModel(models.Model):
    id = models.UUIDField(primary_key=True, default=models.uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    imageUrl = models.URLField()
    rating = models.DecimalField(max_digits=3, decimal_places=2)
    reviewsCount = models.IntegerField()
    brand = models.CharField(max_length=255)

    # ForeignKeys
    supplier = models.ForeignKey(
        "persistence.SupplierModel",
        null=True, blank=True,
        on_delete=models.SET_NULL
    )
    manufacturer = models.ForeignKey(
        "persistence.ManufacturerModel",
        null=True, blank=True,
        on_delete=models.SET_NULL
    )
    category = models.ForeignKey(
        "persistence.CategoryModel",
        null=True, blank=True,
        on_delete=models.SET_NULL
    )