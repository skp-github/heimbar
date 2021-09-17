from django.contrib import admin
from orders.models import Order, OrderItem

# Register your models here.
class OrderItemAdminInline(admin.StackedInline):
   """

   """
   model = OrderItem
   fk_name = 'order'

@admin.register(Order)
class OrderAdminInline(admin.ModelAdmin):

    inlines = (OrderItemAdminInline,)

