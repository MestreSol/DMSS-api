from django.db import models
import uuid

class UserModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(unique=True)
    role = models.ForeignKey(
        "adapters.persistence.RoleModel",
        null=True, blank=True,
        on_delete=models.SET_NULL
    )
