from django.db import models

# menu and booking models
class Menu(models.Model):
   id = models.SmallIntegerField(primary_key=True)
   title = models.CharField(max_length=255) 
   price = models.DecimalField(max_digits=6, decimal_places=2, db_index=True)
   inventory = models.SmallIntegerField(default=0)
   
   def __str__(self):
        return f'{self.title} : {str(self.price)}'

class Booking(models.Model):
    id = models.SmallIntegerField(primary_key=True)
    first_name = models.CharField(max_length=255)
    booking_date = models.DateTimeField()
    no_of_guests = models.SmallIntegerField(default=1)

    def __str__(self): 
        return f'{self.first_name} : {str(self.booking_date)}'



