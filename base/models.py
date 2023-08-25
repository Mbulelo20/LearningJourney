from django.db import models

# Create your models here.
class Journey(models.Model):
    name = models.CharField(max_length=200)
    start_date = '2023/09/11' # Use DateField for date values
    end_date = '2023/09/11'  # Use DateField for date values

    # end_date =  models.DateField()
    updated = (models.DateTimeField(auto_now=True))
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
