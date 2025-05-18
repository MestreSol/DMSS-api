from api_dmss.core import models


class InventoryItemModel(models.Model):
    id = models.UUIDField(primary_key=True, default=models.uuid.uuid4, editable=False)
    quantity = models.IntegerField()
    expirationDate = models.DateField()
    # ForeignKeys
    market = models.ForeignKey(
        "persistence.MarketModel",
        null=True, blank=True,
        on_delete=models.SET_NULL
    )
    palette = models.ForeignKey(
        "persistence.PaletteModel",
        null=True, blank=True,
        on_delete=models.SET_NULL
    )
    product = models.ForeignKey(
        "persistence.ProductModel",
        null=True, blank=True,
        on_delete=models.SET_NULL
    )