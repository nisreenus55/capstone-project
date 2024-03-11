from django.db import models

# Create your models here.
class Booking(models.Model):
    first_name = models.CharField(max_length=200)
    no_of_guests = models.IntegerField()
    reservation_date = models.DateField()
    # reservation_slot = models.SmallIntegerField(default=10)

    def __str__(self): 
        return self.first_name


# Add code to create Menu model
class Menu(models.Model):
    title = models.CharField(max_length=255) 
    price = models.DecimalField(decimal_places=2, max_digits=10, db_index=True)
    inventory = models.IntegerField() 

#    menu_item_description = models.TextField(max_length=1000, default='') 

    def __str__(self):
      return self.title