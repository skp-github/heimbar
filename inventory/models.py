from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils.timezone import now
# Create your models here.
DRINK_TYPE = (
    (0, _('Beer')),
    (1, _('Wine')),
    (2, _('Cider')),
    (3, _('Vodka')),
    (4, _('Gin')),
    (5, _('Whiskey')),
    (6, _('Rum')),
    (7, _('Tequila')),
    (8, _('Brandy')),
    (9, _('Bitters')),
    (10, _('Alcopops')),
    (11, _('Absinthe')),
    (12, _('Amaretto')),
    (13, _('Aperol')),
    (14, _('Averna')),
    (15, _('Baileys')),
    (16, _('Campari')),
    (17, _('Chambord')),
    (18, _('Creme de anything')),
    (19, _('Drambuie')),
    (20, _('Fireball')),
    (21, _('Frangelico')),
    (22, _('Galliano')),
    (23, _('Goldschlager')),
    (24, _('Jagermeister')),
    (25, _('Kahlua')),
    (26, _('Limoncello')),
    (27, _('Maraschino')),
    (28, _('Midori')),
    (29, _('Ouzo')),
    (30, _('Patron XO Cafe')),
    (31, _('Pastis')),
    (32, _('Sambuca')),
    (33, _('Sloe Gin')),
    (34, _('Southern Comfort')),
    (35, _('St Germain')),
    (36, _('Tia Maria')),
    (37, _('Tripel Sec')),
    (38, _('Tuaca')),
    (38, _('Cola')),
)

class Brand(models.Model):
    name = models.CharField(max_length=200)
    created_date = models.DateTimeField('date_created', default=now)
    drink_type = models.PositiveSmallIntegerField(choices=DRINK_TYPE, default=0)
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class Drink(models.Model):
    brand_name = models.ForeignKey(Brand, related_name='brand_name', on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0, verbose_name="quantity in ml")
    drink_name = models.CharField(max_length=200, null=True, blank=True)
    actual_price = models.FloatField()
    sale_price = models.FloatField()
    created_date = models.DateTimeField('date_created', default=now)
    status = models.BooleanField(default=False)
    def __str__(self):
        return self.drink_name

class DrinkInventory(models.Model):
    drink = models.ForeignKey(Drink, related_name='drink', on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)
    created_date = models.DateTimeField('date_created', default=now)
    status = models.BooleanField(default=False)
    def __str__(self):
        return self.drink.drink_name

class Cocktail(models.Model):
    name = models.CharField(max_length=200)
    ingredients = models.CharField(max_length=200)
    created_date = models.DateTimeField('date_created', default=now)
    sale_price = models.FloatField()
    status = models.BooleanField(default=False)
    image = models.ImageField(upload_to='images')
    def __str__(self):
        return self.name

class Mocktail(models.Model):
    name = models.CharField(max_length=200)
    ingredients = models.CharField(max_length=200)
    sale_price = models.FloatField()
    created_date = models.DateTimeField('date_created', default=now)
    status = models.BooleanField(default=False)
    image = models.ImageField(upload_to='images')

    def __str__(self):
        return self.name

class Shisha(models.Model):
    name = models.CharField(max_length=200)
    rent_price = models.FloatField()
    created_date = models.DateTimeField('date_created', default=now)
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.name