from api_dmss.core import models


class EconomicStateModel(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField()
    gdp = models.DecimalField(max_digits=15, decimal_places=2)
    inflation_rate = models.DecimalField(max_digits=5, decimal_places=2)
    unemployment_rate = models.DecimalField(max_digits=5, decimal_places=2)
    interest_rate = models.DecimalField(max_digits=5, decimal_places=2)
    
    # ForeignKey relationships
    region = models.ForeignKey('Region', on_delete=models.CASCADE, related_name='economic_states')
    products = models.ManyToManyField('Product', related_name='economic_states')
    