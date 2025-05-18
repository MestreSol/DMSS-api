from api_dmss.core import models


class MarketModel(models.Model):
    id = models.UUIDField(primary_key=True, default=models.uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    description = models.TextField()
    
