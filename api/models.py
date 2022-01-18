from django.db import models
from django.core.validators import MaxValueValidator

# Create your models here.

class Timings(models.Model):
    opening_time_mon = models.IntegerField(validators=[MaxValueValidator(2359)])
    closing_time_mon = models.IntegerField(validators=[MaxValueValidator(2359)])

    opening_time_tue = models.IntegerField(validators=[MaxValueValidator(2359)])
    closing_time_tue = models.IntegerField(validators=[MaxValueValidator(2359)])
    
    opening_time_wed = models.IntegerField(validators=[MaxValueValidator(2359)])
    closing_time_wed = models.IntegerField(validators=[MaxValueValidator(2359)])
    
    opening_time_thu = models.IntegerField(validators=[MaxValueValidator(2359)])
    closing_time_thu = models.IntegerField(validators=[MaxValueValidator(2359)])
    
    opening_time_fri = models.IntegerField(validators=[MaxValueValidator(2359)])
    closing_time_fri = models.IntegerField(validators=[MaxValueValidator(2359)])
    
    opening_time_sat = models.IntegerField(validators=[MaxValueValidator(2359)])
    closing_time_sat = models.IntegerField(validators=[MaxValueValidator(2359)])
    
    opening_time_sun = models.IntegerField(validators=[MaxValueValidator(2359)])
    closing_time_sun = models.IntegerField(validators=[MaxValueValidator(2359)])

class Restaurant(models.Model):
    name = models.CharField(max_length=255)
    type = models.CharField(max_length=255)
    desc = models.CharField(max_length=9999)
    timings = models.ForeignKey(Timings, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} | {self.type} | {self.desc} |{self.timings}"
