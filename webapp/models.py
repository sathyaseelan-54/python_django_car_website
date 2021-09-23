from django.db import models

# Create your models here.

class Booking(models.Model):
    name = models.CharField(max_length = 100);
    email = models.EmailField(max_length = 100 );
    phone = models.IntegerField(null = False,blank = False,unique = True);
    model = models.CharField(max_length = 100);
    departure_date = models.DateTimeField();
    return_data = models.DateTimeField();

    def __str__(self):
        return self.name




