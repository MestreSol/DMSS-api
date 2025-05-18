from api_dmss.core import models


class PlayerModel(models.Model):
    id = models.UUIDField(primary_key=True, default=models.uuid.uuid4, editable=False)
    experience = models.DecimalField(max_digits=10, decimal_places=2)
    level = models.IntegerField()

    user = models.OneToOneField(
        "persistence.UserModel",
        null=True, blank=True,
        on_delete=models.SET_NULL
    )

