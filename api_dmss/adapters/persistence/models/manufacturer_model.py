from api_dmss.core import models


class ManufacturerModel(models.Model):
    id = models.UUIDField(primary_key=True, default=models.uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    description = models.TextField()
    logoUrl = models.URLField()
    country = models.CharField(max_length=255)

    # ForeignKeys
    category = models.ForeignKey(
        "persistence.CategoryModel",
        null=True, blank=True,
        on_delete=models.SET_NULL
    )
    