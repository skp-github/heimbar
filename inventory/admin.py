from django.contrib import admin
from inventory.models import Brand, DrinkInventory, Drink, Mocktail, Cocktail, Shisha

# Register your models here.

class DrinkAdminInline(admin.StackedInline):
   """

   """
   model = Drink
   fk_name = 'brand_name'

@admin.register(Brand)
class BrandAdminInline(admin.ModelAdmin):
    inlines = (DrinkAdminInline,)

@admin.register(Drink)
class Drink(admin.ModelAdmin):
    """"""

@admin.register(DrinkInventory)
class DrinkInventoryAdmin(admin.ModelAdmin):
    """

    """
    # list_display = ['information_type', 'title', 'information', 'high_secure', 'created', 'modified', 'created_by', 'updated_by']
    # search_fields = ['title']
    # list_filter = ['created', 'modified', 'created_by', 'updated_by', 'information_type', 'information']
    # inlines = (BrandAdminInline, DrinkAdminInline)

@admin.register(Mocktail)
class Mocktail(admin.ModelAdmin):
    """"""

@admin.register(Cocktail)
class Cocktail(admin.ModelAdmin):
    """"""
@admin.register(Shisha)
class Shisha(admin.ModelAdmin):
    """"""