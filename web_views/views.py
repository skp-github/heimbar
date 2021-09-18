from django.shortcuts import render
from django.views.generic import ListView
from inventory.models import Cocktail, Mocktail, Drink
from orders.models import Order, OrderItem
from datetime import date

# Create your views here.
class SpecialsListView(ListView):
    template_name = 'web/special/specials_list.html'

    def get_queryset(self):
        qs = {}
        qs["cocktails"] = Cocktail.objects.filter(created_date__date=date.today())
        qs["mocktails"] = Mocktail.objects.filter(created_date__date=date.today())
        return qs

    # def get_context_data(self, *, object_list=None, **kwargs):
    #     ctx = super().get_context_data(object_list=object_list, **kwargs)
    #     ctx['count'] = get_panel_count(self.request.user)
    #     return ctx

class SalesOverviewListView(ListView):
    template_name = 'web/heimbar/sales_analytics.html'

    def get_queryset(self):
        qs = {}
        orders = Order.objects.all()
        total_sales = 0
        qs['number_of_orders'] = len(orders)
        for order_loop in orders:
            total_sales += order_loop.total_price
        qs['total_sales'] = total_sales
        drinks = Drink.objects.all()
        cocktails = Cocktail.objects.all()
        mocktails = Mocktail.objects.all()
        drink_count = {}
        for drink in drinks:
            drink_count[drink.drink_name] = OrderItem.objects.filter(drink=drink).count()
        # for cocktail in cocktails:
        #     drink_count[cocktail.name] = OrderItem.objects.filter(cocktail=cocktail).count()
        # for mocktail in mocktails:
        #     drink_count[mocktail.name] = OrderItem.objects.filter(mocktail=mocktail).count()
        qs['drinks_sale_count'] = drink_count

        return qs
