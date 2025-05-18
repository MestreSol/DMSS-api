from api_dmss.core import models


class RegionModel(models.Model):
    id = models.UUIDField(primary_key=True, default=models.uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    description = models.TextField()
    population = models.IntegerField()
    
    # ForeignKeys
    localCurrency = models.ForeignKey(
        "persistence.CurrencyModel",
        null=True, blank=True,
        on_delete=models.SET_NULL
    )