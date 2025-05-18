from api_dmss.core import models


class PaletteModel(models.Model):
    id = models.UUIDField(primary_key=True, default=models.uuid.uuid4, editable=False)
    code = models.CharField(max_length=255)
    productQuantity = models.IntegerField()
    expirationDate = models.DateField()
    #foreign keys
    manufacturer = models.ForeignKey(
        "persistence.ManufacturerModel",
        null=True, blank=True,
        on_delete=models.SET_NULL
    )
    product = models.ForeignKey(
        "persistence.ProductModel",
        null=True, blank=True,
        on_delete=models.SET_NULL
    )
    supplierEmissor = models.ForeignKey(
        "persistence.SupplierModel",
        null=True, blank=True,
        on_delete=models.SET_NULL
    )