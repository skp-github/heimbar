from django.db import models
from inventory.models import Drink, Mocktail, Cocktail, Shisha
from django.utils.timezone import now
# Create your models here.
class Order(models.Model):
    created_date = models.DateTimeField('date_created', default=now)
    total_price = models.DecimalField(max_digits=7, decimal_places=2)

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.PROTECT)
    drink = models.ForeignKey(Drink, on_delete=models.PROTECT, null=True, blank=True)
    drink_quantity = models.IntegerField(default=0)
    mocktail = models.ForeignKey(Mocktail, on_delete=models.PROTECT, null=True, blank=True)
    mocktail_quantity = models.IntegerField(default=0)
    cocktail = models.ForeignKey(Cocktail, on_delete=models.PROTECT, null=True, blank=True)
    cocktail_quantity = models.IntegerField(default=0)
    shisha = models.ForeignKey(Shisha, on_delete=models.PROTECT, null=True, blank=True)
    shisha_quantity = models.IntegerField(default=0)
    created_date = models.DateTimeField('date_created', default=now)
