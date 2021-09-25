from django.shortcuts import render
from django.views.generic import ListView
from inventory.models import Cocktail, Mocktail, Drink
from orders.models import Order, OrderItem
from datetime import date, datetime, timedelta



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
        timediff = datetime.now() - timedelta(hours=48)
        orders = Order.objects.filter(created_date__gte=timediff)
        total_sales = 0
        qs['number_of_orders'] = len(orders)
        for order_loop in orders:
            total_sales += order_loop.total_price
        qs['total_sales'] = total_sales
        drinks = Drink.objects.all()
        cocktails = Cocktail.objects.all()
        mocktails = Mocktail.objects.all()
        drink_count = {}
        qs['total_drinks_served'] = 0
        for drink in drinks:
            total_drink_served  = 0
            for oo in OrderItem.objects.filter(drink=drink):
                total_drink_served += oo.drink_quantity
            drink_count[drink.drink_name] = total_drink_served
            qs['total_drinks_served'] += total_drink_served
        for cocktail in cocktails:
            total_drink_served = 0
            for oo in OrderItem.objects.filter(cocktail=cocktail):
                total_drink_served += oo.cocktail_quantity
            drink_count[cocktail.name] = total_drink_served
            qs['total_drinks_served'] += total_drink_served
        for mocktail in mocktails:
            total_drink_served = 0
            for oo in OrderItem.objects.filter(mocktail=mocktail):
                total_drink_served += oo.mocktail_quantity
            drink_count[mocktail.name] = total_drink_served
            qs['total_drinks_served'] += total_drink_served
        qs['drinks_count'] = drink_count
        return qs
