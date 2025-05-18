from api_dmss.core import models


class CurrencyModel(models.Model):
    id = models.UUIDField(primary_key=True, default=models.uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    description = models.TextField()
    symbol = models.CharField(max_length=10)
    exchangeRate = models.DecimalField(max_digits=10, decimal_places=2)