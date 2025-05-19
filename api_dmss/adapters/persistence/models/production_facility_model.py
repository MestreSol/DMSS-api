from api_dmss.core import models


class production_facility_model(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, unique=True)
    location = models.CharField(max_length=255)
    capacity = models.IntegerField()
    operational_status = models.BooleanField(default=True)    
    
    #ForeignKey relationships
    region = models.ForeignKey('Region', on_delete=models.CASCADE, related_name='production_facilities')
    products = models.ManyToManyField('Product', related_name='production_facilities')
    