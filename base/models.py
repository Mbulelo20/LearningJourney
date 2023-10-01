from django.db import models

# Create your models here.




class Journey(models.Model):
    name = models.CharField(max_length=200)
    tag = models.CharField(null=True,max_length=20)
    start_date = models.DateField() # Use DateField for date values

    end_date =  models.DateField()
    updated = (models.DateTimeField(auto_now=True))
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
         ordering = ['-updated','-created']
         
    def __str__(self):
        return self.name
    
class Chapter(models.Model):

    journey = models.ForeignKey(Journey, on_delete=models.CASCADE)
    title = models.CharField(max_length=20)
    body = models.TextField()

    class Meta:
        unique_together = ('journey', 'title')
        
    def __str__(self):
            return self.title