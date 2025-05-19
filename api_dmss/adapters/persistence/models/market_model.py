from api_dmss.core import models


class MarketModel(models.Model):
    id = models.UUIDField(primary_key=True, default=models.uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    description = models.TextField()
    level = models.IntegerField()
    confortLevel = models.IntegerField()
    expereince = models.DecimalField(max_digits=10, decimal_places=2)
    reputation = models.DecimalField(max_digits=10, decimal_places=2)
    
    user = models.OneToOneField(
        "persistence.UserModel",
        null=True, blank=True,
        on_delete=models.SET_NULL
    )
    region = models.ForeignKey(
        "persistence.RegionModel",
        null=True, blank=True,
        on_delete=models.SET_NULL
    )
    
