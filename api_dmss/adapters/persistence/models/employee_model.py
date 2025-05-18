from api_dmss.core import models


class EmployeeModel(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    position = models.CharField(max_length=100, blank=True, null=True)
    department = models.CharField(max_length=100, blank=True, null=True)
    hire_date = models.DateField(blank=True, null=True)
    salary = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    workLevel = models.IntegerField(blank=True, null=True)
    fatigue = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    
    # ForeignKeys
    market = models.ForeignKey(
        "persistence.MarketModel",
        null=True, blank=True,
        on_delete=models.SET_NULL
    )
    personalityTraits = models.ForeignKey(
        "persistence.PersonalityTraitsModel",
        null=True, blank=True,
        on_delete=models.SET_NULL
    )

