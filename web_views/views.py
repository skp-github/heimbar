from django.shortcuts import render
from django.views.generic import ListView
from inventory.models import Cocktail, Mocktail
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
